"""Testing dictionary.py."""

__author__ = "730664291"

import pytest
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_key_error() -> None:
    """When values within a dictionary are the same, inverting them will raise a KeyError as there'd be duplicate keys."""
    with pytest.raises(KeyError):
        """test_list_dupes should return a KeyError."""
        input_dict = {'Bob': 'Ross', 'Jaiden': 'Ross'}
        invert(input_dict)


def test_list_names() -> None:
    """test_list_names should return last names assigned to a first name."""
    input_dict = {'Austin': 'Hill', 'Sean': 'Crowl'}
    assert invert(input_dict) == {'Hill': 'Austin', 'Crowl': 'Sean'}


def test_list_numbers() -> None:
    """test_list_numbers should assign numbers names."""
    input_dict = {'Austin': '1', 'Sean': "2", 'Tristan': "3"}
    assert invert(input_dict) == {'1': 'Austin', '2': 'Sean', '3': 'Tristan'}


def test_color_red() -> None:
    """test_color_red should return red."""
    input_dict = {'Tristan': 'blue', 'Austin': 'orange', 'Sean': 'orange', 'Jayden': 'orange'}
    assert favorite_color(input_dict) == "orange"


def test_no_colors() -> None:
    """test_no_colors should return chips."""
    input_dict = {'Tristan': 'chips', 'Austin': 'pizza', 'Sean': 'chips', 'Jayden': 'pizza'}
    assert favorite_color(input_dict) == "chips"


def test_color_yellow() -> None:
    """test_no_colors should return yellow."""
    input_dict = {'Tristan': 'yellow', 'Austin': 'yellow', 'Sean': 'yellow', 'Jayden': 'purple', 'Antonio': 'purple'}
    assert favorite_color(input_dict) == "yellow"


def test_count_empty() -> None:
    """Empty list inputed returns and empty dictionary."""
    input_list = []
    assert count(input_list) == {}


def test_count_names() -> None:
    """List of names will be assigned a value of how many times it appears."""
    input_list = ['Austin', 'Austin', 'Sean', 'Tristan', 'Tristan', 'Tristan']
    assert count(input_list) == {'Austin': 2, 'Sean': 1, 'Tristan': 3}


def test_count_numbers() -> None:
    """List of numbers will be assigned a value for how much it appears."""
    input_list = ['1', '1', '1', '1', '1', '2', '2', '3', '3', '4', '4', '4']
    assert count(input_list) == {'1': 5, '2': 2, '3': 2, '4': 3}


def test_alphabetizer_abc() -> None:
    """List of strings will create a keys b and t assigning values when index 0 == key."""
    input_list = ['bus', 'tire', 'boy', 'truck', 'toy']
    assert alphabetizer(input_list) == {'b': ['bus', 'boy'], 't': ['tire', 'truck', 'toy']}

    
def test_alphabetizer_empty() -> None:
    """List of strings will create a keys b and t assigning values when index 0 == key."""
    input_list = []
    assert alphabetizer(input_list) == {}


def test_alphabetizer_faw() -> None:
    """List of strings will create a keys f, a, and w assigning values when index 0 == key even when index 0 is capitalized."""
    input_list = ['Fair', 'foul', 'Ample', 'west', 'word']
    assert alphabetizer(input_list) == {'f': ['Fair', 'foul'], 'a': ['Ample'], 'w': ['west', 'word']}


def test_update_attendance_empty() -> None:
    """Update an empty dictionary."""
    input_dict = {}
    day = "Thursday"
    student = "Josh"
    assert update_attendance(input_dict, day, student) == {'Thursday': ['Josh']}


def test_update_attendance_duplicate() -> None:
    """When given duplicate names, the function will not add the duplicate name to the respective day inputed."""
    input_dict = {'Monday': ['Jake', 'Tristan', 'Jayden', 'Eve'], 'Tuesday': ['Shikha', 'Heather', 'Jay'], 'Wednesday': ['Eve', 'Tristan', 'Jay']}
    day = "Monday"
    student = "Eve"
    assert update_attendance(input_dict, day, student) == {'Monday': ['Jake', 'Tristan', 'Jayden', 'Eve'], 'Tuesday': ['Shikha', 'Heather', 'Jay'], 'Wednesday': ['Eve', 'Tristan', 'Jay']}


def test_update_attendance_new_day() -> None:
    """When given a new day, a new key is established and assigned a name in a list."""
    input_dict = {'Monday': ['Jeff', 'Caroline', 'Alex'], 'Tuesday': ['Tristan', 'Autumn', 'Teresa']}
    day = "Wednesday"
    student = "Austin"
    assert update_attendance(input_dict, day, student) == {'Monday': ['Jeff', 'Caroline', 'Alex'], 'Tuesday': ['Tristan', 'Autumn', 'Teresa'], 'Wednesday': ["Austin"]}