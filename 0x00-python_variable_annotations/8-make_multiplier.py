#!/usr/bin/env python3

""" A function to create a multiplier function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Creates a multiplier function """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
