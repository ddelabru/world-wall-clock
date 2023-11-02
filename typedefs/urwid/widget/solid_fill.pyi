from .constants import Sizing as Sizing
from .widget import Widget as Widget
from _typeshed import Incomplete
from urwid.canvas import SolidCanvas as SolidCanvas

class SolidFill(Widget):
    ignore_focus: bool
    fill_char: Incomplete
    def __init__(self, fill_char: str = ...) -> None: ...
    def render(self, size: tuple[int, int], focus: bool = ...) -> SolidCanvas: ...
