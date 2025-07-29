#!/usr/bin/env python3

"""Module to measure the runtime of wait_n."""

import time
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n(n, max_delay).
    Args:
        n: Number of times to run.
        max_delay: Maximum delay for each coroutine.
    Returns:
        Average time per coroutine.
    """
    start = time.time()
    import asyncio
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n
