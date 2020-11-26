import pytest

from unbuiltins import first


def test_list():
    assert first(["a", "b"]) == "a"


def test_list_empty():
    with pytest.raises(TypeError):
        _ = first([])

    assert first([], "default") == "default"


def test_iterator():
    assert first(iter(["a", "b"])) == "a"


def test_iterator_empty():
    with pytest.raises(TypeError):
        _ = first(iter([]))

    assert first(iter([]), "default") == "default"
