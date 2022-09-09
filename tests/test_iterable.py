import pytest

from satchel.iterable import chunk

_params = [
    {"lst_length": 3, "n": 3, "as_list": True, "_expected": 1},
    {"lst_length": 6, "n": 3, "as_list": True, "_expected": 2},
    {"lst_length": 10, "n": 3, "as_list": True, "_expected": 4},
    {"lst_length": 12, "n": 3, "as_list": True, "_expected": 4},
]


@pytest.mark.parametrize("params", _params)
def test_chunk_by_length(params):
    print(params)
    chunks = chunk(
        list(range(params["lst_length"])),
        params["n"],
        mode="length",
        as_list=True,
    )
    assert len(chunks) == params["_expected"]


@pytest.mark.parametrize("params", _params)
def test_chunk_by_count(params):
    print(params)
    chunks = chunk(
        list(range(params["lst_length"])),
        params["n"],
        mode="count",
        as_list=True,
    )
    assert len(chunks) == params["n"]
