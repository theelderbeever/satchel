from collections import defaultdict
from typing import Callable, Iterable, Literal, TypeVar

T = TypeVar("T")
K = TypeVar("K")
R = TypeVar("R")

_apply_methods = {"count": len}


def _groupby(it: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    d = defaultdict(list)
    for i in it:
        d[key(i)].append(i)
    return d


def groupapply(
    it: Iterable[T],
    key: Callable[[T], K] = lambda x: x,
    apply: Literal["count"] | Callable[[list[T]], R] = "count",
) -> dict[K, R]:
    if isinstance(apply, str):
        apply = _apply_methods.get(apply, None)
        if apply is None:
            raise ValueError(
                f"Argument `apply` must be a callable or {list(_apply_methods.keys())}"
            )
    return {k: apply(g) for k, g in _groupby(it, key).items()}
