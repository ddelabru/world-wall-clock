from _typeshed import Incomplete
from urwid.widget import (
    BarGraph as BarGraph,
    BarGraphError as BarGraphError,
    BarGraphMeta as BarGraphMeta,
    BigText as BigText,
    GraphVScale as GraphVScale,
    LineBox as LineBox,
    ProgressBar as ProgressBar,
    Widget,
    scale_bar_values as scale_bar_values,
)

class PythonLogo(Widget):
    def __init__(self) -> None: ...
    def pack(self, size: Incomplete | None = ..., focus: bool = ...): ...
    def render(self, size, focus: bool = ...): ...
