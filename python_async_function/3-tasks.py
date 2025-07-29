#!/usr/bin/env python3

"""Module for creating asyncio tasks from wait_random."""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> "asyncio.Task[float]":
    """
    Return an asyncio.Task for wait_random with max_delay.
    Args:
        max_delay: Maximum delay for the wait_random coroutine.
    Returns:
        An asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
