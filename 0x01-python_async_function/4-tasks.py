#!/usr/bin/env python3
'''
module of the wait_n coroutine
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''function that calculate wait_n'''
    x = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    return sorted(x)
