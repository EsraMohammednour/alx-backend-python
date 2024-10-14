#!/usr/bin/env python3
'''modul to do async code'''
import asyncio
import random


async def wait_random(max_delay=10):
    '''async function that take value annd wait and then return it'''

    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
