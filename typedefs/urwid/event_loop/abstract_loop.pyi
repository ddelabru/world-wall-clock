# mypy: ignore-errors

import abc
import signal
import typing
from collections.abc import Callable
from types import FrameType

class ExitMainLoop(Exception): ...

class EventLoop(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def alarm(
        self, seconds: float, callback: Callable[[], typing.Any]
    ) -> typing.Any: ...
    @abc.abstractmethod
    def enter_idle(self, callback): ...
    @abc.abstractmethod
    def remove_alarm(self, handle) -> bool: ...
    @abc.abstractmethod
    def remove_enter_idle(self, handle) -> bool: ...
    @abc.abstractmethod
    def remove_watch_file(self, handle) -> bool: ...
    @abc.abstractmethod
    def run(self) -> None: ...
    @abc.abstractmethod
    def watch_file(self, fd: int, callback: Callable[[], typing.Any]): ...
    def set_signal_handler(
        self,
        signum: int,
        handler: Callable[[int, FrameType | None], typing.Any] | int | signal.Handlers,
    ) -> (
        Callable[[int, FrameType | None], typing.Any] | int | signal.Handlers | None
    ): ...
