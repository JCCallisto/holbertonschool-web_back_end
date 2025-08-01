#!/usr/bin/env python3

"""Module for asynchronous coroutine that waits for a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds.
    Args:
        max_delay: Maximum number of seconds to wait (inclusive).
    Returns:
        The random delay as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
