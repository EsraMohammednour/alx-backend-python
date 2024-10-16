#!/usr/bin/env python3
'''type-annotated function'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' function make_multiplier that takes a float
    multiplier as argument and returns a function
    that multiplies a float by multiplier'''
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
