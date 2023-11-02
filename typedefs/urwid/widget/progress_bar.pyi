# mypy: ignore-errors

from .constants import Align as Align, Sizing as Sizing, WrapMode as WrapMode
from .text import Text as Text
from .widget import Widget as Widget
from _typeshed import Incomplete
from urwid.canvas import TextCanvas as TextCanvas

class ProgressBar(Widget):
    eighths: str
    text_align: Incomplete
    normal: Incomplete
    complete: Incomplete
    satt: Incomplete
    def __init__(
        self,
        normal,
        complete,
        current: int = ...,
        done: int = ...,
        satt: Incomplete | None = ...,
    ) -> None: ...
    def set_completion(self, current) -> None: ...
    current: Incomplete
    @property
    def done(self): ...
    def rows(self, size, focus: bool = ...) -> int: ...
    def get_text(self) -> str: ...
    def render(self, size: tuple[int], focus: bool = ...) -> TextCanvas: ...
