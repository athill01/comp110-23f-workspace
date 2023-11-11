"""Combining two lists into a dictionary."""

__author__ = "730664291"


def zip(x: list[str], y: list[int]) -> dict[str, int]:
    """Combining list x and list y into a dictionary."""
    if len(x) != len(y):
        return dict()
    i = 0
    dictionary = dict()
    for idx in x:
        dictionary[idx] = y[i]
        i += 1
    return dictionary