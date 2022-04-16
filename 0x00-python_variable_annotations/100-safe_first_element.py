#!/usr/bin/env python3
'''Task 10's module.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''If exists, return first element of `lst`.
    '''
    if lst:
        return lst[0]
    else:
        return None
