"""Implementing utility functions with lists."""

__author__ = "730664291"


def all(list: list[int], value: int) -> bool:
    """Determines if all values are equal to the inputed integer."""
    if len(list) == 0:
        return False
    list_idx: int = 0
    while list_idx < len(list):
        if list[list_idx] == value:
            list_idx += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Pulls the max number from a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 0
    high_n = input[list_idx]
    while list_idx < len(input):
        if input[list_idx] > high_n:
            high_n = input[list_idx]
        else:
            list_idx += 1
    return high_n


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if each corresponding index within a list is equal."""
    if len(list1) != len(list2):
        return False
    idx: int = 0
    while idx < len(list1):
        if list1[idx] == list2[idx]:
            idx += 1
        else:
            return False
    return True