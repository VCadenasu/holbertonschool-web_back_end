#!/usr/bin/env python

"""
asynchronous coroutine that takes in an integer argument
That waits for a random delay
Return the value
"""
import random
import asyncio


async def wait_random(max_delay = 10):
    """Make a randon number within 0 and max_delay"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
