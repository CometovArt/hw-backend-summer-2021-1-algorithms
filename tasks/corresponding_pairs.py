from typing import TypeVar
from collections import deque

__all__ = ("corresponding_pairs",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def corresponding_pairs(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    """Формирует список пар из пары списков.

    Example:
        >> corresponding_pairs([1, 2], [3, 4])
        [(1, 3), (2, 4)]
    """
    
    min_lengs_list = min(len(arr1), len(arr2))
    
    if not min_lengs_list:
        return []
        
    return [(arr1[i], arr2[i]) for i in range(min_lengs_list)]