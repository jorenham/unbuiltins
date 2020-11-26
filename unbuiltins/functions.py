__all__ = ["first", "optional_set"]

from typing import Iterable, Optional, Set, TypeVar

from unbuiltins.constants import Missable, Missing

T = TypeVar("T")


def first(iterable: Iterable[T], /, default: Missable[T] = Missing) -> T:
    """
    first(iterable[, default])

    Return the first item from the iterable. If default is given and the
    iteratable has no next item, it is returned instead of raising TypeError
    """
    v = next(iter(iterable), default)
    if v is Missing:
        raise TypeError("first() of empty iterable")
    else:
        return v


def optional_set(value: Missable[Optional[Iterable[T]]] = Missing, /) -> Set[T]:
    """
    set() -> new empty set object
    set(Missing) -> new empty set object
    set(None) -> new empty set object
    set(iterable) -> new set object

    Alias for set() that allows to pass None as argument.
    """
    if value is Missing or value is None:
        return set()
    else:
        return set(value)
