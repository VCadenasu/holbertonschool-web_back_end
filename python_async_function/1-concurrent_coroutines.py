#!/usr/bin/env python3

"""
Async routine cwai_n
Takes in 2 int arguments n and max_delay
Return the list of all the delays in float value.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    task = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*task)
    delays.extend(results)
    return sorted(delays)
