import json
import runpy
import tempfile
from datetime import tzinfo
from pathlib import Path
from typing import Optional
from unittest import TestCase, mock
from zoneinfo import ZoneInfo

import urwid
import urwid.html_fragment

from world_wall_clock import wwclock


class TestModule(TestCase):
    @mock.patch("world_wall_clock.wwclock.main")
    def test_exec_world_wall_clock_module(self, wwclock_main: mock.Mock) -> None:
        runpy.run_module("world_wall_clock")
        wwclock_main.assert_called()

    @mock.patch("world_wall_clock.wwclock.parse_args")
    @mock.patch("world_wall_clock.wwclock.App")
    def test_print_ver(self, app_cls: mock.Mock, parse_args: mock.Mock) -> None:
        args: mock.MagicMock = mock.MagicMock()
        args.version = True
        parse_args.return_value = args
        wwclock.main()
        app_cls.assert_not_called()

    @mock.patch("sys.argv", new=["wwclock"])
    @mock.patch("world_wall_clock.wwclock.App")
    def test_keyboard_interrupt(self, app_cls: mock.Mock) -> None:
        def raise_keyboard_interrupt() -> None:
            raise KeyboardInterrupt()

        app: mock.MagicMock = mock.MagicMock()
        app.main_loop.run.side_effect = raise_keyboard_interrupt
        app_cls.return_value = app
        wwclock.main()
        app.main_loop.run.assert_called()


class TestApp(TestCase):
    app: wwclock.App.get_config_path
    temp: tempfile.NamedTemporaryFile

    def setUp(self) -> None:
        self.temp = tempfile.NamedTemporaryFile("x")
        f = self.temp.__enter__()
        config_file = Path(f.name)
        self.app = wwclock.App()
        self.app.get_config_path = lambda: config_file

    def cleanUp(self) -> None:
        self.temp.__exit__()

    @mock.patch("json.dump")
    def test_recover_from_write_clock_list_os_error(self, dump: mock.Mock) -> None:
        def mock_json_dump(o, f) -> None:
            raise OSError("Mock json.dump OSError")

        dump.side_effect = mock_json_dump
        self.app.write_clock_list()
        assert self.app

    def test_app_handle_input(self) -> None:
        assert self.app.handle_input("e") is False
        with self.assertRaises(urwid.ExitMainLoop):
            self.app.handle_input("q")

    def test_config_path_recovers_from_mkdir_error(self) -> None:
        def mock_mkdir(*args, **kwargs) -> None:
            raise OSError("mock mkdir error")

        with mock.patch("pathlib.Path.mkdir", side_effect=mock_mkdir):
            config_path: Path = self.app.get_config_path()
            assert isinstance(config_path, Path)

    def test_update_clocks_if_current(self) -> None:
        self.app.current = False
        with mock.patch.object(self.app, "update_clocks") as mock_update:
            self.app.update_clocks_if_current()
            mock_update.assert_not_called()
            self.app.current = True
            self.app.update_clocks_if_current()
            mock_update.assert_called_once()

    def test_change_date_switches_to_custom_time(self) -> None:
        assert self.app.current is True
        self.app.dp.year.set_edit_text("1968")
        self.app.dp.day.set_edit_text("28")
        self.app.dp.month.set_edit_text("07")
        self.app.dp.month.set_edit_text("12")
        assert self.app.current is False

    def test_write_clock_list(self) -> None:
        with open(self.app.get_config_path(), "w") as f:
            f.write("")
        self.app.foreign_clocks = self.app.load_clock_list()
        assert self.app.foreign_clocks == wwclock.DEFAULT_CLOCKS
        self.app.write_clock_list()
        with open(self.app.get_config_path(), "r") as f:
            assert json.load(f).get("clocks") == wwclock.DEFAULT_CLOCKS

    def test_load_default_clock_list(self) -> None:
        with open(self.app.get_config_path(), "w") as f:
            f.write('{"clocks": ["invalid timezone spec"]}\n')
        assert self.app.load_clock_list() == []

    def test_select_deselect_clock(self) -> None:
        cols = self.app.main_loop.widget
        pile = cols.contents[0][0]
        listbox = pile.contents[1][0]
        first_cb = listbox.contents[0][0]
        default_foreign_clocks_len = len(self.app.foreign_clocks)
        first_cb.toggle_state()
        assert len(self.app.foreign_clocks) != default_foreign_clocks_len
        first_cb.toggle_state()
        assert len(self.app.foreign_clocks) == default_foreign_clocks_len


class TestAppScreenshotRun(TestCase):
    def test_run_app(self) -> None:
        urwid.display.html_fragment.screenshot_init([(80, 25)], [["q"]])
        app = wwclock.App()
        app.main_loop.run()
        assert urwid.display.html_fragment.screenshot_collect()


class TestAppGetConfigPath(TestCase):
    app: wwclock.App

    def setUp(self):
        self.app = wwclock.App()

    def test_config_path_recovers_from_mkdir_error(self) -> None:
        def fail_mkdir(*args, **kwargs) -> None:
            raise OSError("mock mkdir error")

        with mock.patch("pathlib.Path.mkdir", side_effect=fail_mkdir) as mock_mkdir:
            config_path: Path = self.app.get_config_path()
            mock_mkdir.assert_called()
            assert isinstance(config_path, Path)


class TestDatetimeIntEdit(TestCase):
    year_edit: wwclock.DatetimeIntEdit

    def setUp(self) -> None:
        dp = wwclock.DatetimePicker()
        dp.month = wwclock.MonthEdit(5, dp)
        dp.day = wwclock.DayEdit(1, dp)
        self.year_edit = wwclock.YearEdit(2064, dp)

    def test_keypress(self) -> None:
        for digit in "1997":
            self.year_edit.keypress((4,), digit)
        assert self.year_edit.value() == 1997
        assert self.year_edit.edit_pos == 3
        self.year_edit.keypress((10,), "backspace")
        assert self.year_edit.edit_pos == 2
        self.year_edit.keypress((10,), "delete")
        assert self.year_edit.edit_pos == 3
        assert self.year_edit.keypress((10,), "up") == "up"
        assert self.year_edit.keypress((10,), "tab") == "right"


class TestTZPicker(TestCase):
    tzpicker: wwclock.ActiveTZPicker

    def setUp(self) -> None:
        self.tzpicker = wwclock.ActiveTZPicker(wwclock.DEFAULT_CLOCKS)

    def test_tzpicker_base_cls(self) -> None:
        super(wwclock.ActiveTZPicker, self.tzpicker).append("UTC")
        super(wwclock.ActiveTZPicker, self.tzpicker).remove("UTC")
        tz = super(wwclock.ActiveTZPicker, self.tzpicker).get_tz()
        assert isinstance(tz, Optional[tzinfo])

    def test_active_tz_picker(self) -> None:
        mock_tz_str: str = "mock_timezone"
        self.tzpicker.append(mock_tz_str)
        assert len(self.tzpicker.list_walker) == len(wwclock.DEFAULT_CLOCKS) + 2
        self.tzpicker.remove(mock_tz_str)
        assert len(self.tzpicker.list_walker) == len(wwclock.DEFAULT_CLOCKS) + 1
        assert self.tzpicker.get_tz() is None
        self.tzpicker.keypress((10, 1), "down")
        assert self.tzpicker.get_tz() is ZoneInfo(wwclock.DEFAULT_CLOCKS[0])
