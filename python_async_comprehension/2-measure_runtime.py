#!/usr/bin/env python3

"""Module to measure runtime of four parallel async comprehensions."""

import asyncio
import time
from typing import Awaitable

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times in parallel and return
    the total execution time.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
