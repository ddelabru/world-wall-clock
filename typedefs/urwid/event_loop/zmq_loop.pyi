import typing
from collections.abc import Callable as Callable

import zmq

from .abstract_loop import EventLoop as EventLoop, ExitMainLoop as ExitMainLoop

ZMQAlarmHandle = typing.TypeVar("ZMQAlarmHandle")
ZMQQueueHandle = typing.TypeVar("ZMQQueueHandle")
ZMQFileHandle = typing.TypeVar("ZMQFileHandle")
ZMQIdleHandle = typing.TypeVar("ZMQIdleHandle")

class ZMQEventLoop(EventLoop):
    def __init__(self) -> None: ...
    def alarm(
        self, seconds: float, callback: Callable[[], typing.Any]
    ) -> ZMQAlarmHandle: ...
    def remove_alarm(self, handle: ZMQAlarmHandle) -> bool: ...
    def watch_queue(
        self, queue: zmq.Socket, callback: Callable[[], typing.Any], flags: int = ...
    ) -> ZMQQueueHandle: ...
    def watch_file(
        self, fd: int, callback: Callable[[], typing.Any], flags: int = ...
    ) -> ZMQFileHandle: ...
    def remove_watch_queue(self, handle: ZMQQueueHandle) -> bool: ...
    def remove_watch_file(self, handle: ZMQFileHandle) -> bool: ...
    def enter_idle(self, callback: Callable[[], typing.Any]) -> ZMQIdleHandle: ...
    def remove_enter_idle(self, handle: ZMQIdleHandle) -> bool: ...
    def run(self) -> None: ...
