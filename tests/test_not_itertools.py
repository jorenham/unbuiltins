import hypothesis.strategies as st
import pytest
from hypothesis import given

from unbuiltins import either, filternone, first


def test_either():
    assert either(None, None, "spam", "ham") == "spam"


def test_either_too_few_args():
    with pytest.raises(TypeError):
        either()
    with pytest.raises(TypeError):
        either("a")


def test_either_all_none():
    with pytest.raises(TypeError):
        either(None, None)


@given(st.iterables(st.one_of(st.integers(), st.none()), max_size=10))
def test_filternone(iterable):
    assert all(i is not None for i in filternone(iterable))


def test_first_list():
    assert first(["a", "b"]) == "a"


def test_first_list_empty():
    with pytest.raises(TypeError):
        _ = first([])

    assert first([], "default") == "default"


def test_first_iterator():
    assert first(iter(["a", "b"])) == "a"


def test_first_iterator_empty():
    with pytest.raises(TypeError):
        _ = first(iter([]))

    assert first(iter([]), "default") == "default"
