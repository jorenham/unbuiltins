__all__ = ["Missing", "Missable"]

from typing import TypeVar, Union

T = TypeVar("T")


class MissingType:
    __slots__ = ()

    def __bool__(self):
        return False

    def __str__(self):
        return "Missing"

    __repr__ = __str__


Missing = MissingType()
Missable = Union[T, MissingType]  # analogue of `typing.Optional[T]`
