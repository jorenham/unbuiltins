import hypothesis.strategies as st
from hypothesis import given

from unbuiltins import frozendict


def test_frozendict_from_nothing():
    fd = frozendict()
    assert not len(fd)
    assert not fd


@given(st.dictionaries(st.integers(), st.text()))
def test_frozendict_from_dict(d):
    fd = frozendict(d)
    assert all(fd[k] == v for k, v in d.items())
    assert fd == d
    assert repr(d) in repr(fd)
    assert str(d) in str(fd)

    d["foo"] = "bar"
    assert "foo" not in fd
    assert fd != d


@given(st.iterables(st.tuples(st.integers(), st.text())))
def test_frozendict_from_iterable(d):
    fd = frozendict(d)
    assert all(fd[k] == v for k, v in d)


@given(st.dictionaries(st.text(), st.text()))
def test_frozendict_from_kwargs(d):
    fd = frozendict(**d)
    assert all(fd[k] == v for k, v in d.items())
    assert fd == d


@given(
    st.dictionaries(st.text(), st.text()),
    st.dictionaries(st.text(), st.integers()),
)
def test_frozendict_from_dict_and_kwargs(d1, d2):
    fd = frozendict(d1, **d2)
    d = {**d1, **d2}
    assert all(fd[k] == v for k, v in d.items())
    assert fd == d
    assert frozendict(d1) | frozendict(d2) == fd


@given(st.dictionaries(st.floats(), st.times()))
def test_frozendict_from_self(d):
    fd1 = frozendict(d)
    fd2 = frozendict(fd1)
    assert all(fd2[k] == v for k, v in fd1.items())
    assert fd1 == fd2
    assert fd2 == d


@given(
    st.dictionaries(st.integers(max_value=100), st.text(), min_size=1),
    st.dictionaries(st.integers(min_value=101), st.text(), min_size=1),
)
def test_frozendict_hash(d1, d2):
    fd1 = frozendict(d1)
    fd2 = frozendict(d2)

    s = set()
    s.add(fd1)

    assert fd1 in s
    assert fd1.copy() in s

    assert fd1 != fd2
    assert fd2 not in s

    s.add(fd2)
    assert fd2 in s
    assert fd1 in s
    assert len(s) == 2


@given(st.dictionaries(st.integers(), st.text()))
def test_frozendict_copy(d):
    fd1 = frozendict(d)
    fd2 = fd1.copy()
    assert fd1 == fd2
    assert fd1 is not fd2


def test_not_equal():
    fd = frozendict(spam="spam")

    assert fd == dict(spam="spam")
    assert fd != dict(spam="spam", eggs="eggs")
    assert fd != dict(spam="not spam")
    assert fd != dict(eggs="eggs")
    assert fd != "spam"
