"""Summing the elements of a list using different loops."""

__author__ = "730664291"


def w_sum(vals: list[float]) -> float:
    """Adding all values in a list."""
    idx = 0
    value: float = 0.0
    while idx < len(vals):
        value += vals[idx]
        idx += 1
    return value


def f_sum(vals: list[float]) -> float:
    """Adding all values in a list."""
    total_value = 0.0
    for value in vals:
        total_value += value
    return total_value


def f_range_sum(vals: list[float]) -> float:
    """Adding all values in a list."""
    total: float = 0.0
    for idx in range(0, len(vals)):
        total += vals[idx]
    return total