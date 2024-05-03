#!/usr/bin/env python3

"""
Type annotated function make_multiplier
Takes a float multiplier as argument
Returns a multiply float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return the result as float"""
    def inner_function(f: float) -> float:
        """Return the inner_function result"""
        return float(f * multiplier)
    return (inner_function)
