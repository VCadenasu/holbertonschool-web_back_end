#!/usr/bin/env python3

"""
A type annotated function sum_list
Takes input_list of floats as argument
Returns the sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Realize the sum and return float"""
    sum = 0
    for val in input_list:
        sum += val
    return float(sum)
