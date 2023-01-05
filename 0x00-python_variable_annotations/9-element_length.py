#!/usr/bin/env python3
""" annotation iterable sequence """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ iterable object """
    return [(i, len(i)) for i in lst]
