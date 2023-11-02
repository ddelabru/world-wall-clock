# mypy: ignore-errors

import typing
from _typeshed import Incomplete
from typing_extensions import Literal
from urwid import escape as escape
from urwid.display_common import (
    AttrSpec as AttrSpec,
    BaseScreen as BaseScreen,
    RealTerminal as RealTerminal,
    UNPRINTABLE_TRANS_TABLE as UNPRINTABLE_TRANS_TABLE,
)

KEY_RESIZE: int
KEY_MOUSE: int

class Screen(BaseScreen, RealTerminal):
    curses_pairs: Incomplete
    palette: Incomplete
    has_color: bool
    s: Incomplete
    cursor_state: Incomplete
    prev_input_resize: int
    last_bstate: int
    def __init__(self) -> None: ...
    def set_mouse_tracking(self, enable: bool = ...) -> None: ...
    max_tenths: Incomplete
    complete_tenths: Incomplete
    resize_tenths: Incomplete
    def set_input_timeouts(
        self,
        max_wait: float | None = ...,
        complete_wait: float = ...,
        resize_wait: float = ...,
    ): ...
    @typing.overload
    def get_input(self, raw_keys: Literal[False]) -> list[str]: ...
    @typing.overload
    def get_input(self, raw_keys: Literal[True]) -> tuple[list[str], list[int]]: ...
    def get_cols_rows(self) -> tuple[int, int]: ...
    keep_cache_alive_link: Incomplete
    def draw_screen(self, size: tuple[int, int], r): ...
    def clear(self) -> None: ...

class _test:
    ui: Incomplete
    l: Incomplete
    def __init__(self) -> None: ...
    def run(self) -> None: ...
