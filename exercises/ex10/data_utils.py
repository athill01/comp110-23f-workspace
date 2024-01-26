"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730664291"

"""Working with CVS data."""


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read CSV file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element of the list
    # for each dictionary (elem), get the value at key "header"
    for elem in table:
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Grabs the first {y} rows in the argument."""
    new_dict: dict[str, list[str]] = {}
    if y > len(x):
        new_dict = x
        return new_dict
    for i in x:
        new_list: list[str] = []
        value = x[i]
        for z in range(0, y):
            new_list.append(value[z])
        new_dict[i] = new_list
    return new_dict


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Will select specfic keys and create a new table providing data connected to them."""
    new_dict: dict[str, list[str]] = {}
    for i in y:
        for z in x:
            if z == i:
                new_dict[i] = x[i]
    return new_dict


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine multiple tables."""
    new_dict: dict[str, list[str]] = {}
    for i in x:
        new_dict[i] = x[i]
    for idx in y:
        if idx in new_dict:
            new_dict[idx] += y[idx]
        else:
            new_dict[idx] = y[idx]
    return new_dict


def count(x: list[str]) -> dict[str, int]:
    """Counts the frequency of values."""
    new_dict: dict[str, int] = {}
    for i in x:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict