#!/usr/bin/env python3

"""
Function task_wait_random
Takes an integer max_delay
Returns a asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio.Task"""
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return (task)
