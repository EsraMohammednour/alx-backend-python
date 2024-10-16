#!/usr/bin/env python3
'''0-async_generator.py'''
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    '''function that generate ramdom float number'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
