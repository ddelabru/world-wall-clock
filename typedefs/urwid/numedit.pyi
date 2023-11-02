from _typeshed import Incomplete
from collections.abc import Container
from decimal import Decimal
from urwid import Edit as Edit

class NumEdit(Edit):
    ALLOWED: str
    def __init__(
        self,
        allowed: Container[str],
        caption,
        default: str | bytes,
        trimLeadingZeros: bool | None = ...,
        *,
        trim_leading_zeros: bool = ...,
        allow_negative: bool = ...,
    ) -> None: ...
    def valid_char(self, ch: str) -> bool: ...
    def keypress(self, size: tuple[int], key: str) -> str | None: ...

class IntegerEdit(NumEdit):
    base: Incomplete
    def __init__(
        self,
        caption: str = ...,
        default: int | str | Decimal | None = ...,
        base: int = ...,
        *,
        allow_negative: bool = ...,
    ) -> None: ...
    def value(self) -> Decimal | None: ...
    def __int__(self) -> int: ...

class FloatEdit(NumEdit):
    significance: Incomplete
    def __init__(
        self,
        caption: str = ...,
        default: str | int | Decimal | None = ...,
        preserveSignificance: bool | None = ...,
        decimalSeparator: str | None = ...,
        *,
        preserve_significance: bool = ...,
        decimal_separator: str = ...,
        allow_negative: bool = ...,
    ) -> None: ...
    def value(self) -> Decimal | None: ...
    def __float__(self) -> float: ...
