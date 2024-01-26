

def free_biscuits(input: dict[str, list[int]]) -> dict[str, bool]:
    """My doc string."""
    # Loop over each key in my input dictionary
    new_dict: dict[str, bool] = {}
    for key in input:
        # for each list, sum up values of list
        list_to_sum: list[int] = input[key]
        sum: int = 0
        #loop through each list and add value to sum
        for elem in list_to_sum:
            sum += elem
        if sum >= 100:
            new_dict[key] = True
        else:
            new_dict[key] = False
    return new_dict

test: dict[str, list[int]] = {"UNCvsDuke": [38, 20, 42], "UNCvsState": [9, 51, 16, 23]}
print(free_biscuits(test))