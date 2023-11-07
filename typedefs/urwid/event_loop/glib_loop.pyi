import signal
import typing
from collections.abc import Callable
from types import FrameType

from typing_extensions import Literal

from .abstract_loop import EventLoop

class GLibEventLoop(EventLoop):
    def __init__(self) -> None: ...
    def alarm(
        self, seconds: float, callback: Callable[[], typing.Any]
    ) -> tuple[int, Callable[[], typing.Any]]: ...
    def set_signal_handler(
        self,
        signum: int,
        handler: Callable[[int, FrameType | None], typing.Any] | int | signal.Handlers,
    ) -> None: ...
    def remove_alarm(self, handle) -> bool: ...
    def watch_file(self, fd: int, callback: Callable[[], typing.Any]) -> int: ...
    def remove_watch_file(self, handle: int) -> bool: ...
    def enter_idle(self, callback: Callable[[], typing.Any]) -> int: ...
    def remove_enter_idle(self, handle) -> bool: ...
    def run(self) -> None: ...
    def handle_exit(
        self, f: Callable[_Spec, _T]
    ) -> Callable[_Spec, _T | Literal[False]]: ...
