"""Dictionary Functions."""

__author__ = "730664291"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a given dictionary with string keys and string values."""
    new_dict: dict[str, str] = {}
    for x in input:
        new_dict[(input[x])] = x
    if len(new_dict) != len(input):
        raise KeyError("ERROR! Duplicate Keys!")
    return new_dict


def favorite_color(x: dict[str, str]) -> str:
    """Identifying which color string appears the most within a dictionar."""
    answer: str = ""
    integer: int = 0
    dict_count: dict[str, int] = {}
    for y in x:
        if x[y] in dict_count:
            dict_count[x[y]] += 1
        else:
            dict_count[x[y]] = 1
    for y in dict_count:
        if dict_count[y] > integer:
            integer = dict_count[y]
            answer = y
    return answer
    

def count(input: list[str]) -> dict[str, int]:
    """Count the amount of times a string appears within a list."""
    new_dict: dict[str, int] = {}
    for item in input:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Organize list provided into letter categories based on the first index."""
    new_dict: dict[str, list[str]] = {}
    for i in input:
        first_letter: str = (i[0].lower())
        if not ((first_letter) in new_dict):
            new_dict[(first_letter)] = []
        new_dict[first_letter].append(i)
            
    return new_dict


def update_attendance(updated: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Given a dictionary of days and names and an additional day and name, update attendance."""
    if not (day in updated):
        updated[day] = []
    if student in updated[day]:
        pass
    else:
        updated[day].append(student)
    return updated