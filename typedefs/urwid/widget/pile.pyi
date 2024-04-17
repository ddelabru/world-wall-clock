# mypy: ignore-errors

from collections.abc import Iterable

from typing_extensions import Literal
from urwid.canvas import (
    CanvasCombine as CanvasCombine,
    CompositeCanvas as CompositeCanvas,
    SolidCanvas as SolidCanvas,
)
from urwid.monitored_list import (
    MonitoredFocusList as MonitoredFocusList,
    MonitoredList as MonitoredList,
)
from urwid.util import is_mouse_press as is_mouse_press

from .constants import Sizing as Sizing, WHSettings as WHSettings
from .container import (
    WidgetContainerListContentsMixin as WidgetContainerListContentsMixin,
    WidgetContainerMixin as WidgetContainerMixin,
)
from .widget import Widget as Widget

class PileError(Exception): ...

class Pile(Widget, WidgetContainerMixin, WidgetContainerListContentsMixin):
    pref_col: int
    def __init__(
        self,
        widget_list: Iterable[
            Widget
            | tuple[Literal["pack", WHSettings.PACK] | int, Widget]
            | tuple[Literal["weight", WHSettings.WEIGHT], int, Widget]
        ],
        focus_item: Widget | int | None = ...,
    ) -> None: ...
    @property
    def widget_list(self): ...
    @property
    def item_types(self): ...
    @property
    def contents(self): ...
    @staticmethod
    def options(
        height_type: Literal["pack", "given", "weight"] = ...,
        height_amount: int | None = ...,
    ) -> tuple[Literal["pack"], None] | tuple[Literal["given", "weight"], int]: ...
    @property
    def focus(self) -> Widget | None: ...
    def get_focus(self) -> Widget | None: ...
    def set_focus(self, item: Widget | int) -> None: ...
    @property
    def focus_item(self): ...
    @property
    def focus_position(self) -> int: ...
    def get_pref_col(self, size): ...
    def get_item_size(
        self,
        size: tuple[int] | tuple[int, int],
        i: int,
        focus: bool,
        item_rows: list[int] | None = ...,
    ) -> tuple[int] | tuple[int, int]: ...
    def get_item_rows(
        self, size: tuple[int] | tuple[int, int], focus: bool
    ) -> list[int]: ...
    def render(self, size, focus: bool = ...): ...
    def get_cursor_coords(
        self, size: tuple[int] | tuple[int, int]
    ) -> tuple[int, int] | None: ...
    def rows(self, size: tuple[int] | tuple[int, int], focus: bool = ...) -> int: ...
    def keypress(self, size: tuple[int] | tuple[int, int], key: str) -> str | None: ...
    def move_cursor_to_coords(
        self, size: tuple[int] | tuple[int, int], col: int, row: int
    ) -> bool: ...
    def mouse_event(
        self,
        size: tuple[int] | tuple[int, int],
        event,
        button: int,
        col: int,
        row: int,
        focus: bool,
    ) -> bool | None: ...
