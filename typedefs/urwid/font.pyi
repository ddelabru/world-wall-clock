import typing
from collections.abc import Iterator, Sequence

from _typeshed import Incomplete
from urwid.canvas import CanvasError as CanvasError, TextCanvas as TextCanvas
from urwid.escape import SAFE_ASCII_DEC_SPECIAL_RE as SAFE_ASCII_DEC_SPECIAL_RE
from urwid.util import (
    apply_target_encoding as apply_target_encoding,
    str_util as str_util,
)

def separate_glyphs(
    gdata: str, height: int
) -> tuple[dict[str, tuple[int, list[str]]], bool]: ...
def add_font(name: str, cls: FontRegistry) -> None: ...

class FontRegistryWarning(UserWarning): ...

class FontRegistry(type):
    def __iter__(self) -> Iterator[str]: ...
    def __getitem__(self, item: str) -> FontRegistry | None: ...
    def __class_getitem__(cls, item: str) -> FontRegistry | None: ...
    @property
    def registered(cls) -> Sequence[str]: ...
    @classmethod
    def as_list(mcs) -> list[tuple[str, FontRegistry]]: ...
    def __new__(
        cls,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, typing.Any],
        **kwds: typing.Any,
    ) -> FontRegistry: ...
    def register(cls, font_name: str) -> None: ...

get_all_fonts: Incomplete

class Font(metaclass=FontRegistry):
    height: int
    data: Sequence[str]
    name: str
    char: Incomplete
    canvas: Incomplete
    utf8_required: bool
    def __init__(self) -> None: ...
    def add_glyphs(self, gdata: str) -> None: ...
    def characters(self) -> str: ...
    def char_width(self, character: str) -> int: ...
    def char_data(self, character: str) -> list[str]: ...
    def render(self, character: str) -> TextCanvas: ...

class Thin3x3Font(Font):
    name: str
    height: int
    data: Incomplete

class Thin4x3Font(Font):
    name: str
    height: int
    data: Incomplete

class Sextant3x3Font(Font):
    name: str
    height: int
    data: Incomplete

class Sextant2x2Font(Font):
    name: str
    height: int
    data: str

class HalfBlock5x4Font(Font):
    name: str
    height: int
    data: Incomplete

class HalfBlock6x5Font(Font):
    name: str
    height: int
    data: str

class HalfBlockHeavy6x5Font(Font):
    name: str
    height: int
    data: str

class Thin6x6Font(Font):
    name: str
    height: int
    data: Incomplete

class HalfBlock7x7Font(Font):
    name: str
    height: int
    data: Incomplete
