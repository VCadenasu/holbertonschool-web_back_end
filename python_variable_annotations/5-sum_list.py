#!/usr/bin/env python3
"""
Sum a list of floats
"""


def sum_list(input_list: list[float]) -> float:
    res = 0
    for val in input_list:
        res += val
    return float(res)
