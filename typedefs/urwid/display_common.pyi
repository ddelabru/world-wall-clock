# mypy: ignore-errors

import typing
from _typeshed import Incomplete
from collections.abc import Iterable
from typing_extensions import Literal, Self
from urwid import signals as signals
from urwid.util import StoppingContext as StoppingContext, int_scale as int_scale

UNPRINTABLE_TRANS_TABLE: Incomplete
UPDATE_PALETTE_ENTRY: str
INPUT_DESCRIPTORS_CHANGED: str
DEFAULT: str
BLACK: str
DARK_RED: str
DARK_GREEN: str
BROWN: str
DARK_BLUE: str
DARK_MAGENTA: str
DARK_CYAN: str
LIGHT_GRAY: str
DARK_GRAY: str
LIGHT_RED: str
LIGHT_GREEN: str
YELLOW: str
LIGHT_BLUE: str
LIGHT_MAGENTA: str
LIGHT_CYAN: str
WHITE: str

class AttrSpecError(Exception): ...

class AttrSpec:
    def __init__(
        self, fg: str, bg: str, colors: Literal[1, 16, 88, 256, 16777216] = ...
    ) -> None: ...
    def copy_modified(
        self,
        fg: str | None = ...,
        bg: str | None = ...,
        colors: Literal[1, 16, 88, 256, 16777216] | None = ...,
    ) -> Self: ...
    def __hash__(self) -> int: ...
    @property
    def foreground_basic(self) -> bool: ...
    @property
    def foreground_high(self) -> bool: ...
    @property
    def foreground_true(self) -> bool: ...
    @property
    def foreground_number(self) -> int: ...
    @property
    def background_basic(self) -> bool: ...
    @property
    def background_high(self) -> bool: ...
    @property
    def background_true(self) -> bool: ...
    @property
    def background_number(self) -> int: ...
    @property
    def italics(self) -> bool: ...
    @property
    def bold(self) -> bool: ...
    @property
    def underline(self) -> bool: ...
    @property
    def blink(self) -> bool: ...
    @property
    def standout(self) -> bool: ...
    @property
    def strikethrough(self) -> bool: ...
    @property
    def colors(self) -> int: ...
    @property
    def foreground(self) -> str: ...
    @property
    def background(self) -> str: ...
    def get_rgb_values(self): ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class RealTerminal:
    def __init__(self) -> None: ...
    def tty_signal_keys(
        self,
        intr: Literal["undefined"] | int | None = ...,
        quit: Literal["undefined"] | int | None = ...,
        start: Literal["undefined"] | int | None = ...,
        stop: Literal["undefined"] | int | None = ...,
        susp: Literal["undefined"] | int | None = ...,
        fileno: int | None = ...,
    ): ...

class ScreenError(Exception): ...

class BaseScreen(metaclass=signals.MetaSignals):
    signals: typing.ClassVar[list[str]]
    def __init__(self) -> None: ...
    @property
    def started(self) -> bool: ...
    def start(self, *args, **kwargs) -> StoppingContext: ...
    def stop(self) -> None: ...
    def run_wrapper(self, fn, *args, **kwargs): ...
    def register_palette(
        self,
        palette: Iterable[
            tuple[str, str]
            | tuple[str, str, str]
            | tuple[str, str, str, str]
            | tuple[str, str, str, str, str, str]
        ],
    ) -> None: ...
    def register_palette_entry(
        self,
        name: str,
        foreground: str,
        background: str,
        mono: str | None = ...,
        foreground_high: str | None = ...,
        background_high: str | None = ...,
    ) -> None: ...
