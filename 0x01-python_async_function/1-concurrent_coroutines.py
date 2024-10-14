#!/usr/bin/env python3
'''
module of the wait_n coroutine
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random
async def wait_n(n, max_delay):
    '''function that calculate wait_n'''
    x = []
    for i in range(n):
        x = await wait_random(max_delay)
        x.append(x)
    return sort(x)
asyncio.run(wait_n(n, max_delay))
