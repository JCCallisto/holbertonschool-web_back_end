#!/usr/bin/env python3

"""Module for executing multiple asyncio tasks concurrently."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with specified max_delay,
    return delays in ascending order.
    Args:
        n: Number of tasks to start.
        max_delay: Maximum delay for each task.
    Returns:
        List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
