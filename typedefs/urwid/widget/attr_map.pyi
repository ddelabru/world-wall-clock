# mypy: ignore-errors

from collections.abc import Hashable

from _typeshed import Incomplete
from urwid.canvas import CompositeCanvas as CompositeCanvas

from .widget import (
    Widget as Widget,
    WidgetError as WidgetError,
    delegate_to_widget_mixin as delegate_to_widget_mixin,
)
from .widget_decoration import WidgetDecoration as WidgetDecoration

class AttrMapError(WidgetError): ...

class AttrMap(Incomplete, WidgetDecoration):
    attr_map: Incomplete
    focus_map: Incomplete
    def __init__(
        self, w: Widget, attr_map, focus_map: Incomplete | None = ...
    ) -> None: ...
    def get_attr_map(self) -> dict[Hashable | None, Hashable]: ...
    def set_attr_map(self, attr_map: dict[Hashable | None, Hashable]) -> None: ...
    def get_focus_map(self) -> dict[Hashable | None, Hashable] | None: ...
    def set_focus_map(self, focus_map: dict[Hashable | None, Hashable]) -> None: ...
    def render(self, size, focus: bool = ...) -> CompositeCanvas: ...
