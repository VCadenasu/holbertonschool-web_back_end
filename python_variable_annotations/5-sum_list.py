#!/usr/bin/env python3

"""
A type annotated function sum_list
Takes input_list of floats as argument
Returns the sum as float
"""


def sum_list(input_list: list[float]) -> float:
    """Realize the sum and return float"""
    x = float(sum(input_list))
    return (x)
 