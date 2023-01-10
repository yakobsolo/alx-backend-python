#!/usr/bin/env python3
""" python async function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ async routine """
    await asyncio.sleep(max_delay*random.random())
    return max_delay*random.random()
