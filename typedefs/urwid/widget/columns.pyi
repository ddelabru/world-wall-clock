# mypy: ignore-errors

from .constants import Align as Align, Sizing as Sizing, WHSettings as WHSettings
from .container import (
    WidgetContainerListContentsMixin as WidgetContainerListContentsMixin,
    WidgetContainerMixin as WidgetContainerMixin,
)
from .widget import Widget as Widget
from _typeshed import Incomplete
from collections.abc import Iterable
from typing_extensions import Literal
from urwid.canvas import (
    CanvasJoin as CanvasJoin,
    CompositeCanvas as CompositeCanvas,
    SolidCanvas as SolidCanvas,
)
from urwid.monitored_list import (
    MonitoredFocusList as MonitoredFocusList,
    MonitoredList as MonitoredList,
)
from urwid.util import is_mouse_press as is_mouse_press

class ColumnsError(Exception): ...

class Columns(Widget, WidgetContainerMixin, WidgetContainerListContentsMixin):
    dividechars: Incomplete
    pref_col: Incomplete
    min_width: Incomplete
    def __init__(
        self,
        widget_list: Iterable[
            Widget
            | tuple[Literal["pack", WHSettings.PACK] | int, Widget]
            | tuple[Literal["weight", WHSettings.WEIGHT], int, Widget]
        ],
        dividechars: int = ...,
        focus_column: int | None = ...,
        min_width: int = ...,
        box_columns: Iterable[int] | None = ...,
    ) -> None: ...
    @property
    def widget_list(self) -> MonitoredList: ...
    @property
    def column_types(self) -> MonitoredList: ...
    @property
    def box_columns(self) -> MonitoredList: ...
    @property
    def has_flow_type(self) -> bool: ...
    @property
    def contents(self): ...
    @staticmethod
    def options(
        width_type: Literal[
            "pack",
            "given",
            "weight",
            WHSettings.PACK,
            WHSettings.GIVEN,
            WHSettings.WEIGHT,
        ] = ...,
        width_amount: int | None = ...,
        box_widget: bool = ...,
    ) -> (
        tuple[Literal[WHSettings.PACK], None, bool]
        | tuple[Literal[WHSettings.GIVEN, WHSettings.WEIGHT], int, bool]
    ): ...
    def set_focus_column(self, num: int) -> None: ...
    def get_focus_column(self) -> int: ...
    def set_focus(self, item: Widget | int) -> None: ...
    @property
    def focus(self) -> Widget | None: ...
    def get_focus(self): ...
    @property
    def focus_position(self) -> int | None: ...
    @property
    def focus_col(self): ...
    def column_widths(
        self, size: tuple[int] | tuple[int, int], focus: bool = ...
    ) -> list[int]: ...
    def render(
        self, size: tuple[int] | tuple[int, int], focus: bool = ...
    ) -> SolidCanvas | CompositeCanvas: ...
    def get_cursor_coords(self, size): ...
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
    def get_pref_col(self, size: tuple[int] | tuple[int, int]) -> int: ...
    def rows(self, size: tuple[int] | tuple[int, int], focus: bool = ...) -> int: ...
    def keypress(self, size: tuple[int] | tuple[int, int], key: str) -> str | None: ...
