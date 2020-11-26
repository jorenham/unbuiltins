__all__ = ["Missing", "Missable"]

import enum
from typing import TypeVar, Union, final

T = TypeVar("T")


@final
class MissingType(enum.Enum):
    # workaround to make type annotation recognize Missing as a singleton
    #  see https://github.com/python/typing/issues/236
    __slots__ = ()

    MISSING = object()

    def __bool__(self):
        return False

    def __str__(self):
        return "Missing"

    __repr__ = __str__


# Missing: Final[MissingType] = MissingType()
Missing = MissingType.MISSING

Missable = Union[T, MissingType]
Missable.__doc__ = """
Missable type, analogous to typing.Optional.

Missable[X] is equivalent to Union[X, Type[Missing]].
"""
