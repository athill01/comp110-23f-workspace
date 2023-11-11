"""Practice functions."""


def odd_and_even(x: list[int]) -> list[int]:
    i: int = 0
    list_2: list[int] = []

    while i < len(x):
        if x[i] % 2 != 0 and i % 2 == 0:
            list_2.append(x[i])
        i += 1
    return list_2

def odd_and_even_for(x: list[int]) -> list[int]:
    list_2: list[int] = []
    for idx in range(0,len(x)-1):
        if x[idx] % 2 != 0 and idx % 2 == 0:
            list_2.append(x[idx])
    return list_2


def value_exists(x: dict[str,int], y: int) -> bool:
    for i in x:
        if x[i] == y:
            return True
    return False


def short_words(og_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = []
    for i in og_list:
        if len(i) < 5:
            new_list.append(i)
        else:
            print(f"{i} is too long!")
    return new_list