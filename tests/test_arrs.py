import pytest

from utils import arrs

coll = [1, 2, 3]


@pytest.fixture
def slice_fixture():
    return coll


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([], 1) == []


def test_slice_f(slice_fixture):
    assert arrs.my_slice(slice_fixture, 1) == [2, 3]
    assert arrs.my_slice(slice_fixture, -4) == [1, 2, 3]
    assert arrs.my_slice(slice_fixture, -3) == [1, 2, 3]
