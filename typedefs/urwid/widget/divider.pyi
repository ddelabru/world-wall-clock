# mypy: ignore-errors

from .constants import Sizing as Sizing
from .widget import Widget as Widget
from _typeshed import Incomplete
from urwid.canvas import CompositeCanvas as CompositeCanvas, SolidCanvas as SolidCanvas

class Divider(Widget):
    ignore_focus: bool
    div_char: Incomplete
    top: Incomplete
    bottom: Incomplete
    def __init__(
        self, div_char: str | bytes = ..., top: int = ..., bottom: int = ...
    ) -> None: ...
    def rows(self, size: tuple[int], focus: bool = ...) -> int: ...
    def render(self, size: tuple[int], focus: bool = ...): ...
