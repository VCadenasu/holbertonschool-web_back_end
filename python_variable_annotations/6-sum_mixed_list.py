#!/usr/bin/env python3

"""
Type annotated function sum_mixed_list
Takes list of integers and floats
Returns the sum as float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all the elements in the list and return a float value"""
    a = 0
    for val in mxd_lst:
        a += val
    return float(a)
