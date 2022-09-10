# Satchel

Satchel is a compendium of pure python functions to carry with you and get things done.

## Installation

```
pip install PySatchel
```

## Usage

```python
>>> import satchel import chunk

>>> some_list = [1, 2, 3, 4, 5]
>>> chunk(some_list, 2, "length", True)
# [[1, 2], [3, 4], [5]]

>>> chunk(some_list, 2, "count", True)
# [[1, 2, 3], [3, 5]]
```

```python
>>> import satchel import groupapply

>>> string = "AAABBAAAACCB"
>>> groupapply(string, apply="count")
# {'A': 7, 'B': 3, 'C': 2}

>>> data = [1, 1, 2, 2, 2, 1, 4]
>>> groupapply(data, key=lambda x: "lower" if x < 3 else "higher", apply="count")
# {'lower': 6, 'higher': 1}

>>> data = [
    {"label": "a", "val": 1},
    {"label": "a", "val": 10},
    {"label": "a", "val": 4},
    {"label": "b", "val": 6},
    {"label": "b", "val": 3},
]

>>> groupapply(data, lambda d: d["label"], lambda l: sum([d["val"] for d in l]))
# {'a': 15, 'b': 9}
```
