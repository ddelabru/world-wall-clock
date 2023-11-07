# mypy: ignore-errors

import typing
from collections.abc import Callable as Callable, Container, Iterable

from _typeshed import Incomplete

class MetaSignals(type):
    def __init__(
        cls, name: str, bases: tuple[type, ...], d: dict[str, typing.Any]
    ) -> None: ...

def setdefaultattr(obj, name, value): ...

class Key: ...

class Signals:
    def __init__(self) -> None: ...
    def register(self, sig_cls, signals: Container[str]) -> None: ...
    def connect(
        self,
        obj,
        name: str,
        callback: Callable[..., typing.Any],
        user_arg: typing.Any = ...,
        *,
        weak_args: Iterable[typing.Any] = ...,
        user_args: Iterable[typing.Any] = ...,
    ) -> Key: ...
    def disconnect(
        self,
        obj,
        name: str,
        callback: Callable[..., typing.Any],
        user_arg: typing.Any = ...,
        *,
        weak_args: Iterable[typing.Any] = ...,
        user_args: Iterable[typing.Any] = ...,
    ) -> None: ...
    def disconnect_by_key(self, obj, name: str, key: Key) -> None: ...
    def emit(self, obj, name: str, *args) -> bool: ...

emit_signal: Incomplete
register_signal: Incomplete
connect_signal: Incomplete
disconnect_signal: Incomplete
disconnect_signal_by_key: Incomplete
