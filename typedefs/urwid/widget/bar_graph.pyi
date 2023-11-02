# mypy: ignore-errors

from .constants import Sizing as Sizing
from .text import Text as Text
from .widget import (
    Widget as Widget,
    WidgetMeta as WidgetMeta,
    nocache_widget_render as nocache_widget_render,
    nocache_widget_render_instance as nocache_widget_render_instance,
)
from _typeshed import Incomplete
from typing_extensions import Literal
from urwid.canvas import (
    CanvasCombine as CanvasCombine,
    CompositeCanvas as CompositeCanvas,
    SolidCanvas as SolidCanvas,
)
from urwid.util import get_encoding_mode as get_encoding_mode

class BarGraphMeta(WidgetMeta):
    def __init__(cls, name, bases, d) -> None: ...

def nocache_bargraph_get_data(self, get_data_fn) -> None: ...

class BarGraphError(Exception): ...

class BarGraph(Widget, metaclass=BarGraphMeta):
    ignore_focus: bool
    eighths: str
    hlines: str
    def __init__(
        self, attlist, hatt: Incomplete | None = ..., satt: Incomplete | None = ...
    ) -> None: ...
    attr: Incomplete
    char: Incomplete
    hatt: Incomplete
    satt: Incomplete
    def set_segment_attributes(
        self, attlist, hatt: Incomplete | None = ..., satt: Incomplete | None = ...
    ) -> None: ...
    data: Incomplete
    def set_data(self, bardata, top, hlines: Incomplete | None = ...) -> None: ...
    bar_width: Incomplete
    def set_bar_width(self, width: int | None): ...
    def calculate_bar_widths(self, size: tuple[int, int], bardata): ...
    def selectable(self) -> Literal[False]: ...
    def use_smoothed(self) -> bool: ...
    def calculate_display(self, size: tuple[int, int]): ...
    def hlines_display(self, disp, top: int, hlines, maxrow: int): ...
    def smooth_display(self, disp): ...
    def render(self, size: tuple[int, int], focus: bool = ...) -> CompositeCanvas: ...

def calculate_bargraph_display(bardata, top, bar_widths, maxrow: int): ...

class GraphVScale(Widget):
    def __init__(self, labels, top) -> None: ...
    pos: Incomplete
    txt: Incomplete
    top: Incomplete
    def set_scale(self, labels, top) -> None: ...
    def selectable(self) -> Literal[False]: ...
    def render(self, size: tuple[int, int], focus: bool = ...): ...

def scale_bar_values(bar, top, maxrow: int): ...
