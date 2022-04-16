#!/usr/bin/env python3
'''Task 7's module
'''
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple(str, float):
    '''Returns a tuple containing `k`, and `v` squared
    '''
    return (k, float(v**2))
