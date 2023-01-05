#!/usr/bin/env python3
""" basic annotation - complex types """
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """ return tuple type str float """
    return (k, v**2)
