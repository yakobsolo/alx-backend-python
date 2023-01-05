#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ callable """
    def fun(n: float):
        return n * multiplier
    return fun
