#!/usr/bin/env python3
'''modlue to type annotated'''
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''to_kv that takes a string k
    and an int OR float v as arguments and returns a tuple.'''
    return (k, float(v ** 2))
