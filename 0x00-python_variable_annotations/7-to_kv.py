#!/usr/bin/env python3
""" basic annotation - complex types """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple type str float """
    return (k, v**2)
