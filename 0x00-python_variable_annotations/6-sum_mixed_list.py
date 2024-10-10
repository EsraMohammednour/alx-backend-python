#!/usr/bin/env python3
''' module to write a function using type annotated'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' function that calculate numbers and return float'''
    return sum(mxd_lst)
