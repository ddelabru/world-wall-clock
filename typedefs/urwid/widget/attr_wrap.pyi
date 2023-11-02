# mypy: ignore-errors

from .attr_map import AttrMap as AttrMap
from .widget import Widget as Widget
from _typeshed import Incomplete

class AttrWrap(AttrMap):
    def __init__(
        self, w: Widget, attr, focus_attr: Incomplete | None = ...
    ) -> None: ...
    @property
    def w(self) -> Widget: ...
    def get_w(self): ...
    original_widget: Incomplete
    def set_w(self, new_widget: Widget) -> None: ...
    def get_attr(self): ...
    def set_attr(self, attr) -> None: ...
    attr: Incomplete
    def get_focus_attr(self): ...
    def set_focus_attr(self, focus_attr) -> None: ...
    focus_attr: Incomplete
    def __getattr__(self, name: str): ...
    def sizing(self): ...