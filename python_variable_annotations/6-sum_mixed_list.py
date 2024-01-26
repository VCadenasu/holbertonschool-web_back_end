#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all list elemnts"""
    res = 0
    for val in mxd_lst:
        res += val
    return float(res)
