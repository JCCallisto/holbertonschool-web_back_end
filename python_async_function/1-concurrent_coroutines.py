#!/usr/bin/env python3

"""Module for executing multiple coroutines concurrently."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with specified max_delay,
    return delays in ascending order.
    Args:
        n: Number of times to spawn wait_random.
        max_delay: Maximum number of seconds to wait for each coroutine.
    Returns:
        List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
