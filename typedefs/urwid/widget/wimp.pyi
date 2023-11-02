# mypy: ignore-errors

import typing
from .columns import Columns as Columns
from .constants import Align as Align, Sizing as Sizing, WrapMode as WrapMode
from .text import Text as Text
from .widget import WidgetWrap as WidgetWrap
from _typeshed import Incomplete
from collections.abc import Callable as Callable, MutableSequence
from typing_extensions import Literal, Self
from urwid.canvas import CompositeCanvas as CompositeCanvas, TextCanvas as TextCanvas
from urwid.command_map import Command as Command
from urwid.signals import connect_signal as connect_signal
from urwid.text_layout import TextLayout as TextLayout, calc_coords as calc_coords
from urwid.util import is_mouse_press as is_mouse_press

class SelectableIcon(Text):
    ignore_focus: bool
    def __init__(
        self,
        text,
        cursor_position: int = ...,
        align: Literal["left", "center", "right"] | Align = ...,
        wrap: Literal["space", "any", "clip", "ellipsis"] | WrapMode = ...,
        layout: TextLayout | None = ...,
    ) -> None: ...
    def render(
        self, size: tuple[int], focus: bool = ...
    ) -> TextCanvas | CompositeCanvas: ...
    def get_cursor_coords(self, size: tuple[int]) -> tuple[int, int] | None: ...
    def keypress(self, size: tuple[int], key: str) -> str: ...

class CheckBoxError(Exception): ...

class CheckBox(WidgetWrap):
    def sizing(self): ...
    states: typing.ClassVar[dict[bool | Literal["mixed"], SelectableIcon]]
    reserve_columns: int
    signals: typing.ClassVar[list[str]]
    @typing.overload
    def __init__(
        self,
        label,
        state: bool = ...,
        has_mixed: typing.Literal[False] = ...,
        on_state_change: Callable[[Self, bool, _T], typing.Any] | None = ...,
        user_data: _T = ...,
        checked_symbol: str | None = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        label,
        state: bool = ...,
        has_mixed: typing.Literal[False] = ...,
        on_state_change: Callable[[Self, bool], typing.Any] | None = ...,
        user_data: None = ...,
        checked_symbol: str | None = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        label: str,
        state: typing.Literal["mixed"] | bool = ...,
        has_mixed: typing.Literal[True] = ...,
        on_state_change: Callable[
            [Self, bool | typing.Literal["mixed"], _T], typing.Any
        ]
        | None = ...,
        user_data: _T = ...,
        checked_symbol: str | None = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        label: str,
        state: typing.Literal["mixed"] | bool = ...,
        has_mixed: typing.Literal[True] = ...,
        on_state_change: Callable[[Self, bool | typing.Literal["mixed"]], typing.Any]
        | None = ...,
        user_data: None = ...,
        checked_symbol: str | None = ...,
    ) -> None: ...
    def pack(
        self, size: tuple[int] | None = ..., focus: bool = ...
    ) -> tuple[str, str]: ...
    def set_label(self, label) -> None: ...
    def get_label(self): ...
    label: Incomplete
    def set_state(
        self, state: bool | Literal["mixed"], do_callback: bool = ...
    ) -> None: ...
    def get_state(self) -> bool | Literal["mixed"]: ...
    state: Incomplete
    def keypress(self, size: tuple[int], key: str) -> str | None: ...
    def toggle_state(self) -> None: ...
    def mouse_event(
        self, size: tuple[int], event, button: int, x: int, y: int, focus: bool
    ) -> bool: ...

class RadioButton(CheckBox):
    states: typing.ClassVar[dict[bool | Literal["mixed"], SelectableIcon]]
    reserve_columns: int
    @typing.overload
    def __init__(
        self,
        group: MutableSequence[CheckBox],
        label,
        state: bool | Literal["first True"] = ...,
        on_state_change: Callable[[Self, bool, _T], typing.Any] | None = ...,
        user_data: _T = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        group: MutableSequence[CheckBox],
        label,
        state: bool | Literal["first True"] = ...,
        on_state_change: Callable[[Self, bool], typing.Any] | None = ...,
        user_data: None = ...,
    ) -> None: ...
    def set_state(
        self, state: bool | Literal["mixed"], do_callback: bool = ...
    ) -> None: ...
    def toggle_state(self) -> None: ...

class Button(WidgetWrap):
    def sizing(self): ...
    button_left: Incomplete
    button_right: Incomplete
    signals: typing.ClassVar[list[str]]
    @typing.overload
    def __init__(
        self,
        label,
        on_press: Callable[[Self, _T], typing.Any] | None = ...,
        user_data: _T = ...,
        *,
        align: Literal["left", "center", "right"] | Align = ...,
        wrap: Literal["space", "any", "clip", "ellipsis"] | WrapMode = ...,
        layout: TextLayout | None = ...,
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        label,
        on_press: Callable[[Self], typing.Any] | None = ...,
        user_data: None = ...,
        *,
        align: Literal["left", "center", "right"] | Align = ...,
        wrap: Literal["space", "any", "clip", "ellipsis"] | WrapMode = ...,
        layout: TextLayout | None = ...,
    ) -> None: ...
    def pack(
        self, size: tuple[int] | None = ..., focus: bool = ...
    ) -> tuple[int, int]: ...
    def set_label(self, label) -> None: ...
    def get_label(self) -> str: ...
    label: Incomplete
    def keypress(self, size: tuple[int], key: str) -> str | None: ...
    def mouse_event(
        self, size: tuple[int], event, button: int, x: int, y: int, focus: bool
    ) -> bool: ...
