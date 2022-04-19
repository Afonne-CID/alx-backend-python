#!/usr/bin/env python3
'''Task 1's module
'''
import asyncio
from typing import List


async_generator = __import__('0-async_comprehension').async_generator


async async_comprehension() -> List[float]:
    '''Collects 10 random numbers using an async comprehensing over
        `async_generator`, then return the 10 random numbers.
    '''
    return [i async for i in async_generator()]
