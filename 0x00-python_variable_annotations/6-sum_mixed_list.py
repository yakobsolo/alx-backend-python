#!/usr/bin/env python3
""" basic annotation - mixed """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return float sum of float and int """
    return sum(mxd_lst)
