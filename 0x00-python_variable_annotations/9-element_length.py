#!/usr/bin/env python3
'''Task 9's module
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns length of a List of sequences
    '''
    return [(i, len(i)) for i in lst]
