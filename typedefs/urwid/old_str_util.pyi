# mypy: ignore-errors

from _typeshed import Incomplete
from typing_extensions import Literal

SAFE_ASCII_RE: Incomplete
SAFE_ASCII_BYTES_RE: Incomplete
widths: list[tuple[int, Literal[0, 1, 2]]]

def get_width(o: int) -> Literal[0, 1, 2]: ...
def decode_one(text: bytes | str, pos: int) -> tuple[int, int]: ...
def decode_one_uni(text: str, i: int) -> tuple[int, int]: ...
def decode_one_right(text: bytes, pos: int) -> tuple[int, int] | None: ...
def set_byte_encoding(enc: Literal["utf8", "narrow", "wide"]): ...
def get_byte_encoding(): ...
def calc_text_pos(
    text: str | bytes, start_offs: int, end_offs: int, pref_col: int
) -> tuple[int, int]: ...
def calc_width(text: str | bytes, start_offs: int, end_offs: int) -> int: ...
def is_wide_char(text: str | bytes, offs: int) -> bool: ...
def move_prev_char(text: str | bytes, start_offs: int, end_offs: int): ...
def move_next_char(text: str | bytes, start_offs: int, end_offs: int) -> int: ...
def within_double_byte(text: bytes, line_start: int, pos: int) -> Literal[0, 1, 2]: ...
def process_east_asian_width() -> None: ...
