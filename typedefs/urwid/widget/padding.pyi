# mypy: ignore-errors

from _typeshed import Incomplete
from typing_extensions import Literal
from urwid.canvas import CompositeCanvas as CompositeCanvas, SolidCanvas as SolidCanvas
from urwid.split_repr import remove_defaults as remove_defaults
from urwid.util import int_scale as int_scale

from .constants import (
    RELATIVE_100 as RELATIVE_100,
    Align as Align,
    Sizing as Sizing,
    WHSettings as WHSettings,
    WrapMode as WrapMode,
    normalize_align as normalize_align,
    normalize_width as normalize_width,
    simplify_align as simplify_align,
    simplify_width as simplify_width,
)
from .widget import Widget as Widget
from .widget_decoration import WidgetDecoration as WidgetDecoration

class PaddingError(Exception): ...

class Padding(WidgetDecoration):
    left: Incomplete
    right: Incomplete
    min_width: Incomplete
    def __init__(
        self,
        w: Widget,
        align: (
            Literal["left", "center", "right"]
            | Align
            | tuple[Literal["relative", WHSettings.RELATIVE], int]
        ) = ...,
        width: (
            int
            | Literal["pack", "clip", WHSettings.PACK, WHSettings.CLIP]
            | tuple[Literal["relative", WHSettings.RELATIVE], int]
        ) = ...,
        min_width: int | None = ...,
        left: int = ...,
        right: int = ...,
    ) -> None: ...
    def sizing(self): ...
    @property
    def align(
        self,
    ) -> Literal["left", "center", "right"] | tuple[Literal["relative"], int]: ...
    @property
    def width(
        self,
    ) -> Literal["clip", "pack"] | int | tuple[Literal["relative"], int]: ...
    def render(
        self, size: tuple[int] | tuple[int, int], focus: bool = ...
    ) -> CompositeCanvas: ...
    def padding_values(
        self, size: tuple[int] | tuple[int, int], focus: bool
    ) -> tuple[int, int]: ...
    def rows(self, size, focus: bool = ...): ...
    def keypress(self, size: tuple[int] | tuple[int, int], key: str) -> str | None: ...
    def get_cursor_coords(
        self, size: tuple[int] | tuple[int, int]
    ) -> tuple[int, int] | None: ...
    def move_cursor_to_coords(
        self, size: tuple[int] | tuple[int, int], x: int, y: int
    ) -> bool: ...
    def mouse_event(
        self,
        size: tuple[int] | tuple[int, int],
        event,
        button: int,
        x: int,
        y: int,
        focus: bool,
    ): ...
    def get_pref_col(self, size: tuple[int] | tuple[int, int]) -> int | None: ...

def calculate_left_right_padding(
    maxcol: int,
    align_type: Literal["left", "center", "right"] | Align,
    align_amount: int,
    width_type: Literal["fixed", "relative", "clip"],
    width_amount: int,
    min_width: int | None,
    left: int,
    right: int,
) -> tuple[int, int]: ...
