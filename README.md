# Thingamabob

That thing or tool that you can't remember what its called but you know you need it. This package is a compendium of pure python functions that don't exist in the std lib but maybe they should?

## Installation

```
pip install thingamabob
```

## Usage

```python
>>> import thingamabob.iterable import chunk

>>> some_list = [1, 2, 3, 4, 5]
>>> chunk(some_list, 2, "length", True)
# [[1, 2], [3, 4], [5]]

>>> chunk(some_list, 2, "count", True)
# [[1, 2, 3], [3, 5]]
```
