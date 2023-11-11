"""Practice with lists."""

grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[1] = "cereal"

grocery_list.pop(2)
grocery_list.append("bananas")
print(grocery_list)

new_dict: dict[str, list[str]] = {}
new_dict['c'] = ("cat")
print(new_dict)