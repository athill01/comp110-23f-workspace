"""Test my zip function."""

__author__ = "730664291"

from lessons.zip import zip


def test_list_empty() -> None:
    """test_list_empty should return 0."""
    test_list_str: list[str] = []
    test_list_int: list[int] = []
    assert zip(test_list_str, test_list_int) == {}


def test_list_days_of_the_week() -> None:
    """test_list_days_of_the_week should return integers assigned to days of the week."""
    test_list_str: list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    test_list_int: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert zip(test_list_str, test_list_int) == {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}


def test_list_of_names() -> None:
    """test_list_of_names should assign each name their respective lengths."""
    test_list_str: list[str] = ["Brandon", "Jeff", "Carlos", "Teresa"]
    test_list_int: list[int] = [7, 4, 6, 6]
    assert zip(test_list_str, test_list_int) == {"Brandon": 7, "Jeff": 4, "Carlos": 6, "Teresa": 6}