"""Dictionary Practice."""

# Create a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# Adding a key,value pair to a dictionary
ice_cream["mint"] = 3
print("Added mint to the dictionary:")

# Removing a key,value pair
ice_cream.pop("mint")
print("Removed mint:")
ice_cream["mint"] = 3

# Accessing and modifying a key,value pair
print(f"There are {ice_cream['chocolate']} orders of chocolate")
ice_cream["vanilla"] += 2

# Print the length
print(f"There are {len(ice_cream)} different orders of ice cream.")

# Check to see if ice cream is in dictionary.
print("Chocolate in Dictionary?")
print("chocolate" in ice_cream)
print("Mint in dictionary?")
print("mint" in ice_cream)

# Using "in" in a conditional
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else:
    print("No orders of mint")

# Loop through dictionary
for flavor in ice_cream:
    print(f"{flavor} has {ice_cream[flavor]} orders.")