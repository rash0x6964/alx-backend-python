#!/usr/bin/env python3
""" A module contains a function that spawns wait_random"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns wait_random n times """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    res = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        res.append(delay)

    return res
