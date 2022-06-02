#!/usr/bin/env python3
'''Task 101 module
'''

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    '''Safely retrives passed value
    '''
    if key in dct:
        return dct[key]
    else:
        return default
