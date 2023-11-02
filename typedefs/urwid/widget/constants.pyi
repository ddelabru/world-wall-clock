# mypy: ignore-errors

import enum
import typing
from _typeshed import Incomplete
from typing_extensions import Literal

class Sizing(str, enum.Enum):
    FLOW: str
    BOX: str
    FIXED: str

class Align(str, enum.Enum):
    LEFT: str
    RIGHT: str
    CENTER: str

class VAlign(str, enum.Enum):
    TOP: str
    MIDDLE: str
    BOTTOM: str

class WrapMode(str, enum.Enum):
    SPACE: str
    ANY: str
    CLIP: str
    ELLIPSIS: str

class WHSettings(str, enum.Enum):
    PACK: str
    GIVEN: str
    RELATIVE: str
    WEIGHT: str
    CLIP: str
    FLOW: str

RELATIVE_100: Incomplete

@typing.overload
def normalize_align(
    align: Literal["left", "center", "right"] | Align, err: type[BaseException]
) -> tuple[Align, None]: ...
@typing.overload
def normalize_align(
    align: tuple[Literal["relative", WHSettings.RELATIVE], int],
    err: type[BaseException],
) -> tuple[Literal[WHSettings.RELATIVE], int]: ...
@typing.overload
def simplify_align(
    align_type: Literal["relative", WHSettings.RELATIVE], align_amount: int
) -> tuple[Literal[WHSettings.RELATIVE], int]: ...
@typing.overload
def simplify_align(
    align_type: Literal["relative", WHSettings.RELATIVE], align_amount: None
) -> typing.NoReturn: ...
@typing.overload
def simplify_align(
    align_type: Literal["left", "center", "right"] | Align, align_amount: int | None
) -> Align: ...
@typing.overload
def normalize_valign(
    valign: Literal["top", "middle", "bottom"] | VAlign, err: type[BaseException]
) -> tuple[VAlign, None]: ...
@typing.overload
def normalize_valign(
    valign: tuple[Literal["relative", WHSettings.RELATIVE], int],
    err: type[BaseException],
) -> tuple[Literal[WHSettings.RELATIVE], int]: ...
@typing.overload
def simplify_valign(
    valign_type: Literal["top", "middle", "bottom"] | VAlign, valign_amount: int | None
) -> VAlign: ...
@typing.overload
def simplify_valign(
    valign_type: Literal["relative", WHSettings.RELATIVE], valign_amount: int
) -> tuple[Literal[WHSettings.RELATIVE], int]: ...
@typing.overload
def simplify_valign(
    valign_type: Literal["relative", WHSettings.RELATIVE], valign_amount: None
) -> typing.NoReturn: ...
@typing.overload
def normalize_width(
    width: Literal["clip", "pack", WHSettings.CLIP, WHSettings.PACK],
    err: type[BaseException],
) -> tuple[Literal[WHSettings.CLIP, WHSettings.PACK], None]: ...
@typing.overload
def normalize_width(
    width: int, err: type[BaseException]
) -> tuple[Literal[WHSettings.GIVEN], int]: ...
@typing.overload
def normalize_width(
    width: tuple[Literal["relative", WHSettings.RELATIVE], int],
    err: type[BaseException],
) -> tuple[Literal[WHSettings.RELATIVE], int]: ...
@typing.overload
def normalize_width(
    width: tuple[Literal["weight", WHSettings.WEIGHT], int], err: type[BaseException]
) -> tuple[Literal[WHSettings.WEIGHT], int]: ...
@typing.overload
def simplify_width(
    width_type: Literal["clip", "pack", WHSettings.CLIP, WHSettings.PACK],
    width_amount: int | None,
) -> Literal[WHSettings.CLIP, WHSettings.PACK]: ...
@typing.overload
def simplify_width(
    width_type: Literal["given", WHSettings.GIVEN], width_amount: int
) -> int: ...
@typing.overload
def simplify_width(
    width_type: Literal["relative", WHSettings.RELATIVE], width_amount: int
) -> tuple[Literal[WHSettings.RELATIVE], int]: ...
@typing.overload
def simplify_width(
    width_type: Literal["weight", WHSettings.WEIGHT], width_amount: int
) -> tuple[Literal[WHSettings.WEIGHT], int]: ...
@typing.overload
def simplify_width(
    width_type: Literal[
        "given",
        "relative",
        "weight",
        WHSettings.GIVEN,
        WHSettings.RELATIVE,
        WHSettings.WEIGHT,
    ],
    width_amount: None,
) -> typing.NoReturn: ...
@typing.overload
def normalize_height(
    height: int, err: type[BaseException]
) -> tuple[Literal[WHSettings.GIVEN], int]: ...
@typing.overload
def normalize_height(
    height: Literal["flow", "pack", Sizing.FLOW, WHSettings.PACK],
    err: type[BaseException],
) -> tuple[Literal[Sizing.FLOW, WHSettings.PACK], None]: ...
@typing.overload
def normalize_height(
    height: tuple[Literal["relative", WHSettings.RELATIVE], int],
    err: type[BaseException],
) -> tuple[Literal[WHSettings.RELATIVE], int]: ...
@typing.overload
def normalize_height(
    height: tuple[Literal["weight", WHSettings.WEIGHT], int], err: type[BaseException]
) -> tuple[Literal[WHSettings.WEIGHT], int]: ...
@typing.overload
def simplify_height(
    height_type: Literal["flow", "pack", WHSettings.FLOW, WHSettings.PACK],
    height_amount: int | None,
) -> Literal[WHSettings.FLOW, WHSettings.PACK]: ...
@typing.overload
def simplify_height(
    height_type: Literal["given", WHSettings.GIVEN], height_amount: int
) -> int: ...
@typing.overload
def simplify_height(
    height_type: Literal["relative", WHSettings.RELATIVE], height_amount: int | None
) -> tuple[Literal[WHSettings.RELATIVE], int]: ...
@typing.overload
def simplify_height(
    height_type: Literal["weight", WHSettings.WEIGHT], height_amount: int | None
) -> tuple[Literal[WHSettings.WEIGHT], int]: ...
@typing.overload
def simplify_height(
    height_type: Literal[
        "relative",
        "given",
        "weight",
        WHSettings.RELATIVE,
        WHSettings.GIVEN,
        WHSettings.WEIGHT,
    ],
    height_amount: None,
) -> typing.NoReturn: ...
