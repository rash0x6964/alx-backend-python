#!/usr/bin/env python3
""" A module that contains parallel comprehensions function """

import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """ Execute async_comprehension four times in parallel """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
