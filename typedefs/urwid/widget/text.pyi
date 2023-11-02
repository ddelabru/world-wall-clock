# mypy: ignore-errors

from .constants import Align as Align, Sizing as Sizing, WrapMode as WrapMode
from .widget import Widget as Widget
from _typeshed import Incomplete
from typing_extensions import Literal
from urwid import text_layout as text_layout
from urwid.canvas import (
    TextCanvas as TextCanvas,
    apply_text_layout as apply_text_layout,
)
from urwid.split_repr import remove_defaults as remove_defaults
from urwid.util import (
    calc_width as calc_width,
    decompose_tagmarkup as decompose_tagmarkup,
)

class TextError(Exception): ...

class Text(Widget):
    ignore_focus: bool
    def __init__(
        self,
        markup,
        align: Literal["left", "center", "right"] | Align = ...,
        wrap: Literal["space", "any", "clip", "ellipsis"] | WrapMode = ...,
        layout: text_layout.TextLayout | None = ...,
    ) -> None: ...
    def set_text(self, markup) -> None: ...
    def get_text(self): ...
    @property
    def text(self) -> str: ...
    @property
    def attrib(self): ...
    def set_align_mode(
        self, mode: Literal["left", "center", "right"] | Align
    ) -> None: ...
    def set_wrap_mode(
        self, mode: Literal["space", "any", "clip", "ellipsis"] | WrapMode
    ) -> None: ...
    def set_layout(
        self,
        align: Literal["left", "center", "right"] | Align,
        wrap: Literal["space", "any", "clip", "ellipsis"] | WrapMode,
        layout: Incomplete | None = ...,
    ) -> None: ...
    align: Incomplete
    wrap: Incomplete
    @property
    def layout(self): ...
    def render(self, size: tuple[int], focus: bool = ...) -> TextCanvas: ...
    def rows(self, size: tuple[int], focus: bool = ...) -> int: ...
    def get_line_translation(self, maxcol: int, ta: Incomplete | None = ...): ...
    def pack(
        self, size: tuple[int] | None = ..., focus: bool = ...
    ) -> tuple[int, int]: ...
