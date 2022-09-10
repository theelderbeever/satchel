from functools import reduce

import pytest

from satchel import groupapply

_params = [
    {"it": "AAABBAACB", "apply": "count", "_expected": {"A": 5, "B": 3, "C": 1}},
    {
        "it": [
            {"key": "a", "val": 1},
            {"key": "a", "val": 1},
            {"key": "a", "val": 1},
            {"key": "b", "val": 2},
            {"key": "b", "val": 2},
        ],
        "key": "key",
        "apply": "count",
        "_expected": {"a": 3, "b": 2},
    },
]


@pytest.mark.parametrize("params", _params)
def test_count(params):
    print(params)
    _expected = params.pop("_expected")
    assert groupapply(**params) == _expected


_params = [
    {
        "it": [1, 1, 1, 2, 2],
        "key": lambda x: x,
        "apply": sum,
        "_expected": {1: 3, 2: 4},
    },
    {
        "it": [1, 1, 1, 2, 2],
        "key": lambda x: x,
        "apply": lambda l: reduce(lambda p, c: p * c, l, 1),
        "_expected": {1: 1, 2: 4},
    },
    {
        "it": [1, 1, 1, 2, 2],
        "key": None,
        "apply": None,
        "_expected": {1: [1, 1, 1], 2: [2, 2]},
    },
    {
        "it": [
            {"key": "a", "val": 1},
            {"key": "a", "val": 1},
            {"key": "a", "val": 1},
            {"key": "b", "val": 2},
            {"key": "b", "val": 2},
        ],
        "key": lambda x: x["key"],
        "apply": lambda l: reduce(lambda p, c: p * c["val"], l, 1),
        "_expected": {"a": 1, "b": 4},
    },
]


@pytest.mark.parametrize("params", _params)
def test_custom_func(params):
    print(params)
    _expected = params.pop("_expected")
    assert groupapply(**params) == _expected


def test_bad_apply_argument():
    with pytest.raises(ValueError):
        groupapply([], apply="do work")
