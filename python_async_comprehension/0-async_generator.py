#!/usr/bin/env python3

"""Module for an asynchronous generator yielding random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield a random float between 0 and 10, ten times,
    with a 1 second delay between yields.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
