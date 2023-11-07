# mypy: ignore-errors

from collections.abc import Sequence

from _typeshed import Incomplete
from urwid import old_str_util as str_util

within_double_byte: Incomplete
SO: str
SI: str
IBMPC_ON: str
IBMPC_OFF: str
DEC_TAG: str
DEC_SPECIAL_CHARS: str
ALT_DEC_SPECIAL_CHARS: str
DEC_SPECIAL_CHARMAP: Incomplete
SAFE_ASCII_DEC_SPECIAL_RE: Incomplete
DEC_SPECIAL_RE: Incomplete

class MoreInputRequired(Exception): ...

def escape_modifier(digit): ...

input_sequences: Incomplete

class KeyqueueTrie:
    data: Incomplete
    def __init__(self, sequences) -> None: ...
    def add(self, root, s, result): ...
    def get(self, keys, more_available: bool): ...
    def get_recurse(self, root, keys, more_available: bool): ...
    def read_mouse_info(self, keys, more_available: bool): ...
    def read_sgrmouse_info(self, keys, more_available: bool): ...
    def read_cursor_position(self, keys, more_available: bool): ...

MOUSE_RELEASE_FLAG: int
MOUSE_MULTIPLE_CLICK_MASK: int
MOUSE_MULTIPLE_CLICK_FLAG: int
MOUSE_DRAG_FLAG: int
input_trie: Incomplete

def process_keyqueue(
    codes: Sequence[int], more_available: bool
) -> tuple[list[str], Sequence[int]]: ...

ESC: str
CURSOR_HOME: Incomplete
CURSOR_HOME_COL: str
APP_KEYPAD_MODE: Incomplete
NUM_KEYPAD_MODE: Incomplete
SWITCH_TO_ALTERNATE_BUFFER: Incomplete
RESTORE_NORMAL_BUFFER: Incomplete
ENABLE_BRACKETED_PASTE_MODE: Incomplete
DISABLE_BRACKETED_PASTE_MODE: Incomplete
REPORT_STATUS: Incomplete
REPORT_CURSOR_POSITION: Incomplete
INSERT_ON: Incomplete
INSERT_OFF: Incomplete

def set_cursor_position(x: int, y: int) -> str: ...
def move_cursor_right(x: int) -> str: ...
def move_cursor_up(x: int) -> str: ...
def move_cursor_down(x: int) -> str: ...

HIDE_CURSOR: Incomplete
SHOW_CURSOR: Incomplete
MOUSE_TRACKING_ON: Incomplete
MOUSE_TRACKING_OFF: Incomplete
DESIGNATE_G1_SPECIAL: Incomplete
ERASE_IN_LINE_RIGHT: Incomplete
