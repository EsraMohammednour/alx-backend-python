#!/usr/bin/env python3
'''module that measure run time'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''function that calculate the total time'''
    run_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - run_time) / n
