#!/usr/bin/env python3
'''Task 2's module
'''
import asyncio
from time import perf_counter
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes `async_comprehension` four times in parallel
        using `asyncio.gather`
    '''
    s = perf_counter()
    task = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*task)
    return perf_counter() - s
