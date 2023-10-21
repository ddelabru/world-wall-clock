#!/usr/bin/env python3

# world-wall-clock, a TUI muitl-timezone clock application
# Copyright (C) 2023 Dominic Delabruere <dominic.delabruere@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from argparse import ArgumentParser, Namespace
from collections.abc import Callable
from datetime import date, datetime, timezone, tzinfo
import json
from pathlib import Path
from typing import Any, Optional
from zoneinfo import available_timezones, ZoneInfo

import urwid
from xdg_base_dirs import xdg_config_home

from . import VERSION


DEFAULT_CLOCKS: list[str] = [
    "Pacific/Niue",
    "America/Santiago",
    "UTC",
    "Europe/Vienna",
    "Africa/Nairobi",
    "Asia/Colombo",
    "Pacific/Auckland",
]


class EventLoop(urwid.SelectEventLoop):
    def __init__(self, update_fn: Callable[[], Any], refresh_rate: float) -> None:
        self.update_fn: Callable[[], Any] = update_fn
        self.tick_secs: float = 1.0 / refresh_rate
        super().__init__()

    def tick(self) -> None:
        self.update_fn()
        self.current_alarm: tuple[float, int, Callable[[], Any]] = self.alarm(
            self.tick_secs, self.tick
        )

    def run(self) -> None:
        self.tick()
        super().run()


class ClockWidget(urwid.LineBox):
    def __init__(
        self,
        tzkey: Optional[str] = None,
        font: urwid.Font = urwid.Thin3x3Font(),
        precision: str = "minutes",
    ) -> None:
        ISO_DATE_LENGTH: int = 10
        self.tzkey: Optional[str] = tzkey
        self.tz: Optional[ZoneInfo] = ZoneInfo(tzkey) if tzkey else None
        self.precision: str = precision
        self._big_text: urwid.BigText = urwid.BigText("", font)
        self._title: Optional[str] = ""
        dt: datetime = self.update_clock()[0]
        clock_size: tuple[int, int] = self._big_text.pack(())
        self._clock_w: int = max(clock_size[0], ISO_DATE_LENGTH)
        self._clock_h: int = clock_size[1]
        iso_date: str = dt.date().isoformat()
        self._date_text: urwid.Text = urwid.Text(iso_date, align="center")
        ideal_width: int = self.get_ideal_width()
        big_padding: urwid.Padding = urwid.Padding(
            self._big_text, align="center", width=None, min_width=ideal_width
        )
        pile: urwid.Pile = urwid.Pile(
            [("pack", big_padding), ("pack", self._date_text)]
        )
        super().__init__(pile, title=self._title)

    def get_ideal_width(self) -> int:
        title: str = self._title or ""
        return max(self._clock_w, len(title) + 4)

    def update_title(self, dt: datetime) -> bool:
        old_title: Optional[str] = self._title
        if isinstance(self.tz, ZoneInfo):
            tz: tzinfo = self.tz
            tzkey: Optional[str] = self.tz.key
            tzname: Optional[str] = tz.tzname(dt)
            self._title = tzkey if tzkey == tzname else f"{tzkey} ({tzname})"
        else:
            dt_utc: datetime = datetime.utcfromtimestamp(dt.timestamp())
            tz = timezone(dt - dt_utc)
            self._title = tz.tzname(dt)
            tzname = tz.tzname(dt)
        if hasattr(self, "title_widget"):
            self.set_title(self._title)
        return old_title != self._title

    def update_clock(self, ts: Optional[float] = None) -> tuple[datetime, bool]:
        dt: datetime = (
            datetime.fromtimestamp(ts, self.tz) if ts else datetime.now(self.tz)
        )
        if hasattr(self, "_date_text"):
            self._date_text.set_text(dt.date().isoformat())
        self._big_text.set_text(dt.time().isoformat(self.precision))
        title_change: bool = self.update_title(dt)
        return dt, title_change

    def pack(
        self, size: Optional[tuple[int]] = None, focus: bool = False
    ) -> tuple[int, int]:
        return self.get_ideal_width() + 2, self._clock_h + 2


class DatetimeIntEdit(urwid.IntEdit):
    def __init__(self, maxlen: int, default: int = 0) -> None:
        self.maxlen: int = maxlen
        padded: str = str(default).rjust(maxlen, "0")
        super().__init__("", padded)

    def keypress(self, size: tuple[int], key: str) -> Optional[str]:
        if self.edit_pos >= self.maxlen:
            self.set_edit_pos(self.maxlen - 1)
        if key in {"up", "down"}:
            return key
        if key == "tab":
            return "right"
        elif key == "backspace":
            return self.keypress(size, "left")
        elif key == "delete":
            return self.keypress(size, "right")
        unhandled: Optional[str] = super(urwid.IntEdit, self).keypress(size, key)
        if self.edit_pos >= self.maxlen:
            self.set_edit_pos(self.maxlen - 1)
            return unhandled or "right"
        return unhandled

    def get_pref_col(self, size: tuple[int]) -> int | str | None:
        return "left"


class DatetimePicker(object):
    def __init__(self) -> None:
        self.year: urwid.IntEdit = DatetimeIntEdit(4)
        self.month: urwid.IntEdit = DatetimeIntEdit(2)
        self.day: urwid.IntEdit = DatetimeIntEdit(2)
        self.hour: urwid.IntEdit = DatetimeIntEdit(2)
        self.mins: urwid.IntEdit = DatetimeIntEdit(2)
        self.tz: urwid.ListBox = urwid.ListBox(urwid.SimpleFocusListWalker([]))


class YearEdit(DatetimeIntEdit):
    def __init__(self, default: int, dp: DatetimePicker) -> None:
        self.dp: DatetimePicker = dp
        super().__init__(4, default)

    def insert_text_result(self, text: str) -> tuple[str, int]:
        if self.edit_pos == 4:
            return self.edit_text, 3
        length: int = len(text)
        if length > 4:
            return self.edit_text, self.edit_pos
        new_text: str = (
            self.edit_text[: self.edit_pos]
            + text
            + self.edit_text[self.edit_pos + length :]
        )
        if len(new_text) > 4:
            return self.edit_text, self.edit_pos
        new_value: int = int(new_text)
        if new_value < 1 and self.edit_pos < 3:
            new_value = 1
        if new_value > 9999 or new_value < 1:
            return self.edit_text, self.edit_pos
        try:
            date(new_value, self.dp.month.value(), self.dp.day.value())
        except ValueError:
            # Handle edge case where setting non-leap year invalidates 29 Feb
            self.dp.day.set_edit_text("28")
        return f"{new_value:04}", self.edit_pos + length


class MonthEdit(DatetimeIntEdit):
    def __init__(self, default: int, dp: DatetimePicker) -> None:
        self.dp: DatetimePicker = dp
        super().__init__(2, default)

    def insert_text_result(self, text: str) -> tuple[str, int]:
        edit_pos: int = self.edit_pos
        if edit_pos == 2:
            return self.edit_text, 1
        length: int = len(text)
        if length > 2:
            return self.edit_text, edit_pos
        new_text: str = (
            self.edit_text[: self.edit_pos]
            + text
            + self.edit_text[self.edit_pos + length :]
        )
        if len(new_text) > 2:
            return self.edit_text, edit_pos
        new_value: int = int(new_text)
        if new_value < 1:
            new_value = 1
        if new_value > 19 and edit_pos == 0:
            new_value = new_value // 10
            edit_pos += 1
        if new_value > 12:
            new_value = 12
        while True:
            day: int = self.dp.day.value()
            try:
                date(self.dp.year.value(), new_value, day)
                break
            except ValueError:
                new_day: int = day - 1
                self.dp.day.set_edit_text(f"{new_day:02}")
        return f"{new_value:02}", edit_pos + length


class DayEdit(DatetimeIntEdit):
    def __init__(self, default: int, dp: DatetimePicker) -> None:
        self.dp: DatetimePicker = dp
        super().__init__(2, default)

    def insert_text_result(self, text: str) -> tuple[str, int]:
        if self.edit_pos == 2:
            return self.edit_text, 1
        length: int = len(text)
        if length > 2:
            return self.edit_text, self.edit_pos
        new_text: str = (
            self.edit_text[: self.edit_pos]
            + text
            + self.edit_text[self.edit_pos + length :]
        )
        if len(new_text) > 2:
            return self.edit_text, self.edit_pos
        new_value: int = int(new_text)
        edit_pos: int = self.edit_pos
        if new_value < 1:
            new_value = 1
        if new_value > 39 and edit_pos == 0:
            new_value = new_value // 10
            edit_pos += 1
        while True:
            try:
                date(self.dp.year.value(), self.dp.month.value(), new_value)
                break
            except ValueError:
                new_value -= 1
        return f"{new_value:02}", self.edit_pos + length


class HourEdit(DatetimeIntEdit):
    def __init__(self, default: int) -> None:
        super().__init__(2, default)

    def insert_text_result(self, text: str) -> tuple[str, int]:
        if self.edit_pos == 2:
            return self.edit_text, 1
        length: int = len(text)
        if length > 2:
            return self.edit_text, self.edit_pos
        new_text: str = (
            self.edit_text[: self.edit_pos]
            + text
            + self.edit_text[self.edit_pos + length :]
        )
        if len(new_text) > 2:
            return self.edit_text, self.edit_pos
        new_value: int = int(new_text)
        edit_pos: int = self.edit_pos
        if new_value < 0:
            new_value = 0
        if new_value > 29 and self.edit_pos == 0:
            new_value = new_value // 10
            edit_pos += 1
        if new_value > 23:
            new_value = 23
        return f"{new_value:02}", edit_pos + length


class MinuteEdit(DatetimeIntEdit):
    def __init__(self, default: int) -> None:
        super().__init__(2, default)

    def insert_text_result(self, text: str) -> tuple[str, int]:
        if self.edit_pos == 2:
            return self.edit_text, 1
        length: int = len(text)
        if length > 2:
            return self.edit_text, self.edit_pos
        new_text: str = (
            self.edit_text[: self.edit_pos]
            + text
            + self.edit_text[self.edit_pos + length :]
        )
        if len(new_text) > 2:
            return self.edit_text, self.edit_pos
        new_value: int = int(new_text)
        edit_pos: int = self.edit_pos
        if new_value < 0:
            new_value = 0
        if new_value > 59 and edit_pos == 0:
            new_value = new_value // 10
            edit_pos += 1
        if new_value > 59:
            new_value = 59
        return f"{new_value:02}", edit_pos + length


class ActiveTZPicker(urwid.ListBox):
    def __init__(self, foreign_clocks: list[str], dp: DatetimePicker) -> None:
        self.dp: DatetimePicker = dp
        self.list_walker: urwid.SimpleFocusListWalker = urwid.SimpleFocusListWalker(
            [], wrap_around=True
        )
        self.update_tz_list(foreign_clocks)
        super().__init__(self.list_walker)

    def update_tz_list(self, foreign_clocks: list[str]) -> None:
        old_focus_item = (
            self.list_walker.get_focus()[0] if len(self.list_walker) else None
        )
        new_items: list[urwid.AttrMap[urwid.Text]] = [
            urwid.AttrMap(urwid.Text("local"), None, "focus")
        ] + [urwid.AttrMap(urwid.Text(tz), None, "focus") for tz in foreign_clocks]
        self.list_walker.clear()
        self.list_walker.extend(new_items)
        try:
            assert old_focus_item is not None
            new_index: int = foreign_clocks.index(old_focus_item.base_widget.text) + 1
            self.list_walker.set_focus(new_index)
        except (AssertionError, ValueError):
            self.list_walker.set_focus(0)

    def get_tz(self) -> Optional[tzinfo]:
        focus_item, focus_index = self.list_walker.get_focus()
        if not focus_index:
            return None
        return ZoneInfo(focus_item.base_widget.text)


class App:
    def __init__(self) -> None:
        self.current: bool = True
        self.foreign_clocks: list[str] = self.load_clock_list()
        self.grid_flow: urwid.GridFlow = urwid.GridFlow(
            [urwid.Text(" ")], 1, 0, 0, "left"
        )
        self.clocks: list[ClockWidget] = [
            ClockWidget(font=urwid.font.HalfBlock5x4Font(), precision="seconds")
        ]
        self.fill_clock_grid(rebuild_clocks=True)
        self.update_clocks()
        grid_filler: urwid.Filler = urwid.Filler(self.grid_flow, valign="top")
        local_clock_width: int = self.clocks[0].pack()[0]

        def cb_postchange(
            cb: urwid.CheckBox, old_state: bool
        ) -> Optional[tuple[urwid.CheckBox, bool]]:
            if old_state:
                self.foreign_clocks.remove(cb.label)
            else:
                self.foreign_clocks.append(cb.label)
            self.write_clock_list()
            self.fill_clock_grid(rebuild_clocks=True)
            return None

        tz_checklist: list[urwid.CheckBox] = [
            urwid.CheckBox(tz, state=(tz in self.foreign_clocks))
            for tz in sorted(available_timezones())
        ]
        for b in tz_checklist:
            urwid.connect_signal(b, "postchange", cb_postchange)
        list_walker: urwid.SimpleFocusListWalker = urwid.SimpleFocusListWalker(
            tz_checklist, wrap_around=True
        )
        list_box: urwid.ListBox = urwid.ListBox(list_walker)
        time_options: list[urwid.RadioButton] = []
        current_button = urwid.RadioButton(
            time_options,
            "Current time",
            state=self.current,
            on_state_change=self.set_current,
        )
        custom_button = urwid.RadioButton(time_options, "Custom time:")
        datetime_editor = self.construct_datetime_editor(datetime.now(), custom_button)
        left_pile: urwid.Pile = urwid.Pile([("pack", self.clocks[0]), list_box])
        right_pile: urwid.Pile = urwid.Pile(
            [grid_filler, ("pack", current_button), ("pack", datetime_editor)]
        )
        columns: urwid.Columns = urwid.Columns(
            [(local_clock_width, left_pile), right_pile]
        )
        event_loop = EventLoop(self.update_clocks_if_current, 10)
        palette = {
            (
                "focus",
                "default,standout",
                "default",
                "standout",
                "default,standout",
                "default",
            )
        }
        self.main_loop: urwid.MainLoop = urwid.MainLoop(
            columns,
            event_loop=event_loop,
            unhandled_input=self.handle_input,
            palette=palette,
        )

    def construct_datetime_editor(
        self, dt: datetime, button: urwid.RadioButton
    ) -> urwid.Columns:
        year, month, day, hour, mins = dt.timetuple()[:5]
        self.dp: DatetimePicker = DatetimePicker()
        self.dp.year = YearEdit(year, self.dp)
        self.dp.month = MonthEdit(month, self.dp)
        self.dp.day = DayEdit(day, self.dp)
        self.dp.hour = HourEdit(hour)
        self.dp.mins = MinuteEdit(mins)
        self.dp.tz = ActiveTZPicker(self.foreign_clocks, self.dp)
        self._new_tz_picker: bool = False
        widgets: list[tuple[int, urwid.Widget]] = [
            (len(button.label) + 5, button),
            (4, self.dp.year),
            (1, urwid.Text("-")),
            (2, self.dp.month),
            (1, urwid.Text("-")),
            (2, self.dp.day),
            (1, urwid.Text(" ")),
            (2, self.dp.hour),
            (1, urwid.Text(":")),
            (2, self.dp.mins),
            (1, urwid.Text(" ")),
            urwid.Padding(urwid.BoxAdapter(self.dp.tz, 1), align="left", width="pack"),
        ]
        for w in (self.dp.year, self.dp.month, self.dp.day, self.dp.hour, self.dp.mins):
            urwid.connect_signal(w, "postchange", self.update_clocks_on_signal)
        urwid.connect_signal(
            self.dp.tz.list_walker, "modified", self.update_clocks_on_signal
        )
        return urwid.Columns(widgets)

    def fill_clock_grid(self, rebuild_clocks: bool = False) -> None:
        if rebuild_clocks:
            self.clocks = self.clocks[:1] + [
                ClockWidget(tzkey) for tzkey in self.foreign_clocks
            ]
        self.grid_flow.contents = [
            (c, self.grid_flow.options(width_amount=c.pack(None)[0]))
            for c in self.clocks[1:]
        ] or [(urwid.Text(" "), self.grid_flow.options())]
        if hasattr(self, "dp"):
            self.dp.tz.update_tz_list(self.foreign_clocks)

    def handle_input(self, key: str) -> None:
        if key in {"q", "Q", "ctrl q", "esc"}:
            raise urwid.ExitMainLoop()

    def update_clocks(self) -> None:
        title_change: bool = False
        if self.current:
            for clock in self.clocks:
                title_change = clock.update_clock()[1] or title_change
        else:
            dt: datetime = datetime(
                self.dp.year.value(),
                self.dp.month.value(),
                self.dp.day.value(),
                self.dp.hour.value(),
                self.dp.mins.value(),
                tzinfo=self.dp.tz.get_tz(),
            )
            ts: float = dt.timestamp()
            for clock in self.clocks:
                title_change = clock.update_clock(ts=ts)[1] or title_change
        if title_change:
            self.fill_clock_grid()

    def update_clocks_on_signal(self, *args, **kwargs) -> None:
        self.update_clocks()

    def update_clocks_if_current(self) -> None:
        if self.current:
            self.update_clocks()

    def set_current(self, cb: urwid.RadioButton, state: bool) -> None:
        self.current = state
        self.update_clocks()

    def get_config_path(self) -> Path:
        config_dir: Path = xdg_config_home() / "wwclock"
        try:
            config_dir.mkdir(exist_ok=True)
        except OSError:
            pass
        return config_dir / "config.json"

    def load_clock_list(self) -> list[str]:
        config_path: Path = self.get_config_path()
        try:
            with open(config_path, "r") as f:
                clocks: list[str] = json.load(f)["clocks"]
            assert type(clocks) == list
            assert all(type(i) == str for i in clocks)
        except Exception:
            clocks = DEFAULT_CLOCKS.copy()

        def load_zone(tzkey: str) -> Optional[tzinfo]:
            try:
                return ZoneInfo(tzkey)
            except Exception:
                return None

        valid_clocks: list[str] = [tzkey for tzkey in clocks if load_zone(tzkey)]
        return valid_clocks

    def write_clock_list(self) -> None:
        config_obj: dict[str, Any] = {"clocks": self.foreign_clocks}
        config_path: Path = self.get_config_path()
        try:
            with open(config_path, "w+", errors="ignore") as f:
                json.dump(config_obj, f)
        except OSError:
            pass


def parse_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="wwclock", description="TUI multi-timezone clock application"
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="Print version number and exit"
    )
    return parser.parse_args()


def main() -> None:
    app: App = App()
    args: Namespace = parse_args()
    if args.version:
        print(VERSION)
        return
    try:
        app.main_loop.run()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
