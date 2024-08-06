#!/usr/bin/env python3
""" A module that contains async generator function """

import asyncio
import random


async def async_generator():
    """ Yield a random number between 0 and 10 """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
