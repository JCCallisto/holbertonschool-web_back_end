#!/usr/bin/env python3

"""Module for creating an asyncio.Task from wait_random."""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task for wait_random with the given max_delay.

    Args:
        max_delay: Maximum number of seconds to wait.

    Returns:
        An asyncio.Task object for wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
