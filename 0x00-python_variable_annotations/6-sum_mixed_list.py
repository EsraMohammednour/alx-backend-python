#!/usr/bin/env python3
''' module to write a function using type annotated'''
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    ''' function that calculate numbers and return float'''
    return sum(mxd_lst)
