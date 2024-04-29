#!/usr/bin/env python3

"""
Annotate the a function parameter
and return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in list"""
    return [(i, len(i)) for i in lst]
