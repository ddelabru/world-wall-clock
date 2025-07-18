# mypy: ignore-errors

import typing

from _typeshed import Incomplete
from typing_extensions import Literal
from urwid import escape as escape, signals as signals, util as util
from urwid.display_common import (
    INPUT_DESCRIPTORS_CHANGED as INPUT_DESCRIPTORS_CHANGED,
    UNPRINTABLE_TRANS_TABLE as UNPRINTABLE_TRANS_TABLE,
    UPDATE_PALETTE_ENTRY as UPDATE_PALETTE_ENTRY,
    AttrSpec as AttrSpec,
    BaseScreen as BaseScreen,
    RealTerminal as RealTerminal,
)

class Screen(BaseScreen, RealTerminal):
    colors: int
    has_underline: bool
    prev_input_resize: int
    screen_buf: Incomplete
    maxrow: Incomplete
    gpm_mev: Incomplete
    gpm_event_pending: bool
    last_bstate: int
    term: Incomplete
    fg_bright_is_bold: Incomplete
    bg_bright_is_blink: Incomplete
    back_color_erase: Incomplete
    signal_handler_setter: Incomplete
    bracketed_paste_mode: Incomplete
    def __init__(
        self, input=..., output=..., bracketed_paste_mode: bool = ...
    ) -> None: ...
    max_wait: Incomplete
    complete_wait: Incomplete
    resize_wait: Incomplete
    def set_input_timeouts(
        self,
        max_wait: Incomplete | None = ...,
        complete_wait: float = ...,
        resize_wait: float = ...,
    ) -> None: ...
    def signal_init(self) -> None: ...
    def signal_restore(self) -> None: ...
    def set_mouse_tracking(self, enable: bool = ...) -> None: ...
    def write(self, data) -> None: ...
    def flush(self) -> None: ...
    @typing.overload
    def get_input(self, raw_keys: Literal[False]) -> list[str]: ...
    @typing.overload
    def get_input(self, raw_keys: Literal[True]) -> tuple[list[str], list[int]]: ...
    def get_input_descriptors(self) -> list[int]: ...
    def unhook_event_loop(self, event_loop) -> None: ...
    def hook_event_loop(self, event_loop, callback): ...
    def get_available_raw_input(self): ...
    def parse_input(self, event_loop, callback, codes, wait_for_more: bool = ...): ...
    def get_cols_rows(self): ...
    def draw_screen(self, maxres, r): ...
    setup_G1: bool
    def clear(self) -> None: ...
    def set_terminal_properties(
        self,
        colors: Incomplete | None = ...,
        bright_is_bold: Incomplete | None = ...,
        has_underline: Incomplete | None = ...,
    ) -> None: ...
    def reset_default_terminal_palette(self): ...
    def modify_terminal_palette(self, entries) -> None: ...
    def AttrSpec(self, fg, bg) -> AttrSpec: ...
