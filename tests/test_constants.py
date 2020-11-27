import hypothesis.strategies as st
import pytest
import typeguard
from hypothesis import given

from unbuiltins import Missable, Missing


def test_missing_identity():
    assert Missing is Missing
    assert Missing == Missing


@given(st.one_of(st.booleans(), st.none(), st.integers(), st.text()))
def test_missing_not_equals(other):
    assert not (Missing is other)
    assert Missing != other


def test_missing_bool():
    assert not Missing


def test_missing_repr():
    assert str(Missing) == repr(Missing) == "Missing"


@pytest.mark.parametrize("missable_str", ["foo", Missing])
def test_missing_type(missable_str: Missable[str]):
    try:
        typeguard.check_argument_types()
    except TypeError:
        type_match = False
    else:
        type_match = True

    assert type_match
