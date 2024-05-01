#!/usr/bin/env python3

"""
Create a function task_wait_n
Takes referencce to wait_n
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the max_delay element"""
    delays = []
    task = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*task)
    delays.extend(results)
    return sorted(delays)
