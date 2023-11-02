# mypy: ignore-errors

import asyncio
import typing
from .abstract_loop import EventLoop
from collections.abc import Callable

class AsyncioEventLoop(EventLoop):
    def __init__(
        self, *, loop: asyncio.AbstractEventLoop | None = ..., **kwargs
    ) -> None: ...
    def alarm(
        self, seconds: float, callback: Callable[[], typing.Any]
    ) -> asyncio.TimerHandle: ...
    def remove_alarm(self, handle) -> bool: ...
    def watch_file(self, fd: int, callback: Callable[[], typing.Any]) -> int: ...
    def remove_watch_file(self, handle: int) -> bool: ...
    def enter_idle(self, callback: Callable[[], typing.Any]) -> int: ...
    def remove_enter_idle(self, handle: int) -> bool: ...
    def run(self) -> None: ...