#!/usr/bin/env python3
"""
A type-annotated function to_kv taking
k string and v int or float as arguments
return a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k as first element and square v"""
    return k, float(v ** 2)
