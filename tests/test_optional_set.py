import hypothesis.strategies as st
from hypothesis import given

from unbuiltins import optional_set


@given(st.lists(st.integers()))
def test_set_equality(iterable):
    assert optional_set(iterable) == set(iterable)


def test_set_empty():
    assert optional_set() == set()


def test_set_none():
    assert optional_set(None) == set()
