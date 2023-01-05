#!/usr/bin/env python3
""" basic annotation - mixed """
from typing import Union

def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """ return float sum of float and int """
    return float(sum(mxd_lst))
