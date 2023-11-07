# mypy: ignore-errors

from _typeshed import Incomplete
from urwid import Font as Font
from urwid.canvas import (
    CanvasJoin as CanvasJoin,
    CompositeCanvas as CompositeCanvas,
    TextCanvas as TextCanvas,
)
from urwid.util import decompose_tagmarkup as decompose_tagmarkup

from .constants import Sizing as Sizing
from .widget import Widget as Widget, fixed_size as fixed_size

class BigText(Widget):
    def __init__(self, markup, font: Font) -> None: ...
    def set_text(self, markup) -> None: ...
    def get_text(self): ...
    font: Incomplete
    def set_font(self, font: Font) -> None: ...
    def pack(self, size: tuple | None = ..., focus: bool = ...) -> tuple[int, int]: ...
    def render(
        self, size: tuple, focus: bool = ...
    ) -> CanvasJoin | CompositeCanvas: ...
