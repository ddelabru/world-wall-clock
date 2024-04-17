# mypy: ignore-errors

from _typeshed import Incomplete
from typing_extensions import Literal
from urwid.canvas import (
    CanvasOverlay as CanvasOverlay,
    CompositeCanvas as CompositeCanvas,
)

from .constants import (
    RELATIVE_100 as RELATIVE_100,
    Align as Align,
    Sizing as Sizing,
    VAlign as VAlign,
    WHSettings as WHSettings,
    WrapMode as WrapMode,
    normalize_align as normalize_align,
    normalize_height as normalize_height,
    normalize_valign as normalize_valign,
    normalize_width as normalize_width,
    simplify_align as simplify_align,
    simplify_height as simplify_height,
    simplify_valign as simplify_valign,
    simplify_width as simplify_width,
)
from .container import (
    WidgetContainerListContentsMixin as WidgetContainerListContentsMixin,
    WidgetContainerMixin as WidgetContainerMixin,
)
from .filler import calculate_top_bottom_filler as calculate_top_bottom_filler
from .padding import calculate_left_right_padding as calculate_left_right_padding
from .widget import Widget as Widget

class OverlayError(Exception): ...

class Overlay(Widget, WidgetContainerMixin, WidgetContainerListContentsMixin):
    top_w: Incomplete
    bottom_w: Incomplete
    def __init__(
        self,
        top_w: Widget,
        bottom_w: Widget,
        align: (
            Literal["left", "center", "right"]
            | Align
            | tuple[
                Literal["relative", "fixed left", "fixed right", WHSettings.RELATIVE],
                int,
            ]
        ),
        width: (
            Literal["pack", WHSettings.PACK]
            | int
            | tuple[Literal["relative", WHSettings.RELATIVE], int]
            | None
        ),
        valign: (
            Literal["top", "middle", "bottom"]
            | VAlign
            | tuple[
                Literal["relative", "fixed top", "fixed bottom", WHSettings.RELATIVE],
                int,
            ]
        ),
        height: (
            Literal["pack", WHSettings.PACK]
            | int
            | tuple[Literal["relative", WHSettings.RELATIVE], int]
            | None
        ),
        min_width: int | None = ...,
        min_height: int | None = ...,
        left: int = ...,
        right: int = ...,
        top: int = ...,
        bottom: int = ...,
    ) -> None: ...
    @staticmethod
    def options(
        align_type: Literal["left", "center", "right", "relative"] | Align,
        align_amount: int | None,
        width_type: Literal["clip", "pack", "relative", "given"] | WHSettings,
        width_amount: int | None,
        valign_type: Literal["top", "middle", "bottom", "relative"] | VAlign,
        valign_amount: int | None,
        height_type: Literal["flow", "pack", "relative", "given"] | WHSettings,
        height_amount: int | None,
        min_width: int | None = ...,
        min_height: int | None = ...,
        left: int = ...,
        right: int = ...,
        top: int = ...,
        bottom: int = ...,
    ): ...
    def set_overlay_parameters(
        self,
        align: (
            Literal["left", "center", "right"]
            | Align
            | tuple[Literal["relative", "fixed left", "fixed right"], int]
        ),
        width: int | None,
        valign: (
            Literal["top", "middle", "bottom"]
            | VAlign
            | tuple[Literal["relative", "fixed top", "fixed bottom"], int]
        ),
        height: int | None,
        min_width: int | None = ...,
        min_height: int | None = ...,
        left: int = ...,
        right: int = ...,
        top: int = ...,
        bottom: int = ...,
    ): ...
    def selectable(self) -> bool: ...
    def keypress(self, size: tuple[int, int], key: str) -> str | None: ...
    @property
    def focus(self) -> Widget: ...
    @property
    def focus_position(self) -> Literal[1]: ...
    @property
    def contents(self): ...
    def _contents__getitem__(self, index: Literal[0, 1]): ...
    align_type: Incomplete
    align_amount: Incomplete
    width_type: Incomplete
    width_amount: Incomplete
    valign_type: Incomplete
    valign_amount: Incomplete
    height_type: Incomplete
    height_amount: Incomplete
    left: Incomplete
    right: Incomplete
    top: Incomplete
    bottom: Incomplete
    min_width: Incomplete
    min_height: Incomplete
    def _contents__setitem__(self, index: Literal[0, 1], value): ...
    def get_cursor_coords(self, size: tuple[int, int]) -> tuple[int, int] | None: ...
    def calculate_padding_filler(
        self, size: tuple[int, int], focus: bool
    ) -> tuple[int, int, int, int]: ...
    def top_w_size(self, size, left, right, top, bottom): ...
    def render(self, size: tuple[int, int], focus: bool = ...) -> CompositeCanvas: ...
    def mouse_event(
        self, size: tuple[int, int], event, button: int, col: int, row: int, focus: bool
    ) -> bool | None: ...
