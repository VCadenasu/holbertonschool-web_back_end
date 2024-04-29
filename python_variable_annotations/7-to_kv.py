#!/usr/bin/env python3

"""
Type annotated function to_kev
Takes a string k and int or float v as arguments
Returns a tuple with k as first element and v square
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """Return the tuple"""
    return (k, float(v ** 2))
