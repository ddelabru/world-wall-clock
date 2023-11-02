# mypy: ignore-errors

from .columns import Columns as Columns
from .constants import Align as Align, Sizing as Sizing
from .divider import Divider as Divider
from .pile import Pile as Pile
from .solid_fill import SolidFill as SolidFill
from .text import Text as Text
from .widget import Widget as Widget, WidgetWrap as WidgetWrap
from .widget_decoration import WidgetDecoration as WidgetDecoration
from _typeshed import Incomplete
from typing_extensions import Literal

class LineBox(WidgetDecoration, WidgetWrap):
    title_widget: Incomplete
    tline_widget: Incomplete
    def __init__(
        self,
        original_widget: Widget,
        title: str = ...,
        title_align: Literal["left", "center", "right"] | Align = ...,
        title_attr: Incomplete | None = ...,
        tlcorner: str = ...,
        tline: str = ...,
        lline: str = ...,
        trcorner: str = ...,
        blcorner: str = ...,
        rline: str = ...,
        bline: str = ...,
        brcorner: str = ...,
    ) -> None: ...
    def format_title(self, text: str) -> str: ...
    def set_title(self, text) -> None: ...
    def pack(
        self, size: Incomplete | None = ..., focus: bool = ...
    ) -> tuple[int, int]: ...
