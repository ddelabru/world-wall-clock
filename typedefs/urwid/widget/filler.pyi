# mypy: ignore-errors

from .constants import (
    RELATIVE_100 as RELATIVE_100,
    Sizing as Sizing,
    VAlign as VAlign,
    WHSettings as WHSettings,
    normalize_height as normalize_height,
    normalize_valign as normalize_valign,
    simplify_height as simplify_height,
    simplify_valign as simplify_valign,
)
from .widget import Widget as Widget
from .widget_decoration import WidgetDecoration as WidgetDecoration
from _typeshed import Incomplete
from typing_extensions import Literal
from urwid.canvas import CompositeCanvas as CompositeCanvas
from urwid.split_repr import remove_defaults as remove_defaults
from urwid.util import int_scale as int_scale

class FillerError(Exception): ...

class Filler(WidgetDecoration):
    top: Incomplete
    bottom: Incomplete
    min_height: Incomplete
    def __init__(
        self,
        body: Widget,
        valign: Literal["top", "middle", "bottom"]
        | VAlign
        | tuple[Literal["relative", WHSettings.RELATIVE], int] = ...,
        height: int | Literal["pack"] | tuple[Literal["relative"], int] | None = ...,
        min_height: int | None = ...,
        top: int = ...,
        bottom: int = ...,
    ) -> None: ...
    def sizing(self): ...
    @property
    def body(self): ...
    def get_body(self): ...
    original_widget: Incomplete
    def set_body(self, new_body) -> None: ...
    def selectable(self) -> bool: ...
    def filler_values(self, size: tuple[int, int], focus: bool) -> tuple[int, int]: ...
    def render(self, size: tuple[int, int], focus: bool = ...) -> CompositeCanvas: ...
    def keypress(self, size: tuple[int, int], key: str) -> str | None: ...
    def get_cursor_coords(self, size: tuple[int, int]) -> tuple[int, int] | None: ...
    def get_pref_col(self, size: tuple[int, int]) -> int: ...
    def move_cursor_to_coords(
        self, size: tuple[int, int], col: int, row: int
    ) -> bool: ...
    def mouse_event(
        self, size: tuple[int, int], event, button: int, col: int, row: int, focus: bool
    ) -> bool: ...

def calculate_top_bottom_filler(
    maxrow: int,
    valign_type: Literal["top", "middle", "bottom", "relative", WHSettings.RELATIVE]
    | VAlign,
    valign_amount: int,
    height_type: Literal[
        "given",
        "relative",
        "clip",
        WHSettings.GIVEN,
        WHSettings.RELATIVE,
        WHSettings.CLIP,
    ],
    height_amount: int,
    min_height: int | None,
    top: int,
    bottom: int,
) -> tuple[int, int]: ...
