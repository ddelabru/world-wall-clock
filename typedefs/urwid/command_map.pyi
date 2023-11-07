# mypy: ignore-errors

import enum
import typing
from typing import Iterator

from _typeshed import Incomplete
from typing_extensions import Self

class Command(str, enum.Enum):
    REDRAW_SCREEN: str
    UP: str
    DOWN: str
    LEFT: str
    RIGHT: str
    PAGE_UP: str
    PAGE_DOWN: str
    MAX_LEFT: str
    MAX_RIGHT: str
    ACTIVATE: str
    MENU: str

REDRAW_SCREEN: Incomplete
CURSOR_UP: Incomplete
CURSOR_DOWN: Incomplete
CURSOR_LEFT: Incomplete
CURSOR_RIGHT: Incomplete
CURSOR_PAGE_UP: Incomplete
CURSOR_PAGE_DOWN: Incomplete
CURSOR_MAX_LEFT: Incomplete
CURSOR_MAX_RIGHT: Incomplete
ACTIVATE: Incomplete

class CommandMap(typing.Mapping[str, typing.Union[str, Command, None]]):
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __init__(self) -> None: ...
    def restore_defaults(self) -> None: ...
    def __getitem__(self, key: str) -> str | Command | None: ...
    def __setitem__(self, key, command: str | Command) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def clear_command(self, command: str | Command) -> None: ...
    def copy(self) -> Self: ...

command_map: Incomplete
