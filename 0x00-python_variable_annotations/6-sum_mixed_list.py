#!/usr/bin/env python3
'''Task 6's module
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''Returns the sum of `mxd_list` as a float
    '''
    return float (sum(mxd_list))
