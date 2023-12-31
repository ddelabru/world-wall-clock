# mypy: ignore-errors

from _typeshed import Incomplete
from typing_extensions import Literal
from urwid.util import (
    calc_text_pos as calc_text_pos,
    calc_trim_text as calc_trim_text,
    calc_width as calc_width,
    is_wide_char as is_wide_char,
    move_next_char as move_next_char,
    move_prev_char as move_prev_char,
)

class TextLayout:
    def supports_align_mode(self, align): ...
    def supports_wrap_mode(self, wrap): ...
    def layout(self, text, width, align, wrap) -> None: ...

class CanNotDisplayText(Exception): ...

class StandardTextLayout(TextLayout):
    def __init__(self) -> None: ...
    def supports_align_mode(self, align: str) -> bool: ...
    def supports_wrap_mode(self, wrap: str) -> bool: ...
    def layout(
        self,
        text,
        width: int,
        align: Literal["left", "center", "right"],
        wrap: Literal["any", "space", "clip", "ellipsis"],
    ): ...
    def pack(self, maxcol: int, layout) -> int: ...
    def align_layout(
        self,
        text,
        width: int,
        segs,
        wrap: Literal["any", "space", "clip", "ellipsis"],
        align: Literal["left", "center", "right"],
    ): ...
    def calculate_text_segments(
        self, text, width: int, wrap: Literal["any", "space", "clip", "ellipsis"]
    ): ...

default_layout: Incomplete

class LayoutSegment:
    text: Incomplete
    end: Incomplete
    def __init__(
        self, seg: tuple[int, int, bytes | int] | tuple[int, int | None]
    ) -> None: ...
    def subseg(self, text, start: int, end: int): ...

def line_width(segs): ...
def shift_line(segs, amount: int): ...
def trim_line(segs, text, start: int, end: int): ...
def calc_line_pos(text, line_layout, pref_col: Literal["left", "right"] | int): ...
def calc_pos(
    text, layout, pref_col: Literal["left", "right"] | int, row: int
) -> int: ...
def calc_coords(text, layout, pos, clamp: int = ...): ...
