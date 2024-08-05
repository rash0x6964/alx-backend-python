#!/usr/bin/env python3
"""A module contains a function waits for a random time"""

import asyncio
import random


async def wait_random(max_delay: int = 10):
    """ Waits for a random delay between 0 and max_delay """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
