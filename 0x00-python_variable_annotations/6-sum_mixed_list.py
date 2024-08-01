#!/usr/bin/env python3
""" A function to sum a list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums up all the integers and floats in the input list """
    return float(sum(mxd_lst))
