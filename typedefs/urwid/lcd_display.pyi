import typing
from collections.abc import Iterable, Sequence

from _typeshed import Incomplete
from typing_extensions import Literal

from .display_common import BaseScreen as BaseScreen

class LCDScreen(BaseScreen):
    def set_terminal_properties(
        self,
        colors: Incomplete | None = ...,
        bright_is_bold: Incomplete | None = ...,
        has_underline: Incomplete | None = ...,
    ) -> None: ...
    def set_mouse_tracking(self, enable: bool = ...) -> None: ...
    def set_input_timeouts(self, *args) -> None: ...
    def reset_default_terminal_palette(self, *args) -> None: ...
    def draw_screen(self, size, r) -> None: ...
    def clear(self) -> None: ...
    def get_cols_rows(self): ...

class CFLCDScreen(LCDScreen):
    KEYS: typing.ClassVar[list[str | None]]
    CMD_PING: int
    CMD_VERSION: int
    CMD_CLEAR: int
    CMD_CGRAM: int
    CMD_CURSOR_POSITION: int
    CMD_CURSOR_STYLE: int
    CMD_LCD_CONTRAST: int
    CMD_BACKLIGHT: int
    CMD_LCD_DATA: int
    CMD_GPO: int
    CMD_KEY_ACTIVITY: int
    CMD_ACK: int
    CURSOR_NONE: int
    CURSOR_BLINKING_BLOCK: int
    CURSOR_UNDERSCORE: int
    CURSOR_BLINKING_BLOCK_UNDERSCORE: int
    CURSOR_INVERTING_BLINKING_BLOCK: int
    MAX_PACKET_DATA_LENGTH: int
    colors: int
    has_underline: bool
    device_path: Incomplete
    def __init__(self, device_path: str, baud: int) -> None: ...
    @classmethod
    def get_crc(cls, buf: bytearray) -> int: ...

    class InvalidPacket(Exception): ...
    class MoreDataRequired(Exception): ...

class KeyRepeatSimulator:
    repeat_delay: Incomplete
    repeat_next: Incomplete
    pressed: Incomplete
    multiple_pressed: bool
    def __init__(self, repeat_delay: float, repeat_next: float) -> None: ...
    def press(self, key: str) -> None: ...
    def release(self, key: str) -> None: ...
    def next_event(self) -> tuple[float, str] | None: ...
    def sent_event(self) -> None: ...

class CF635Screen(CFLCDScreen):
    DISPLAY_SIZE: Incomplete
    CGROM: str
    cursor_style: Incomplete
    repeat_delay: Incomplete
    repeat_next: Incomplete
    key_repeat: Incomplete
    key_map: Incomplete
    def __init__(
        self,
        device_path: str,
        baud: int = ...,
        repeat_delay: float = ...,
        repeat_next: float = ...,
        key_map: Iterable[str] = ...,
    ) -> None: ...
    def get_input_descriptors(self): ...
    def get_input_nonblocking(self) -> tuple[None, list[str], list[int]]: ...
    def queue_command(self, command: int, data: str) -> None: ...
    def draw_screen(self, size: tuple[int, int], canvas): ...
    def program_cgram(self, index: int, data: Sequence[int]) -> None: ...
    def set_cursor_style(self, style: Literal[1, 2, 3, 4]) -> None: ...
    def set_backlight(self, value: int) -> None: ...
    def set_lcd_contrast(self, value: int) -> None: ...
    def set_led_pin(self, led: Literal[0, 1, 2, 3], rg: Literal[0, 1], value: int): ...
