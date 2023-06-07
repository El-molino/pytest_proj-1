from utils.dicts import get_val


def test_dict():
    assert get_val({1: "a"}, 1) == "a"
    assert get_val({1: "a"}, 2) == "git"
    assert get_val({}, 2) == "git"
