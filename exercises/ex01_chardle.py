"""EX01 - Chardle - A cute step toward Worldle."""

__author__ = "730664291"

my_word = input("Enter a 5-character word: ")

if (len(my_word) != 5):
    print("Error: Word must contain 5 characters")
    exit(len(my_word) != 5)

my_character = input("Enter a single character: ")

if (len(my_character) != 1):
    print("Error: Character must be a single character.")
    exit(len(my_word) != 1)

count: int = 0

print("Searching for " + my_character + " in " + my_word)

if (my_word[0] == my_character):
    print(my_character + " found at index 0")
    count += 1
if (my_word[1] == my_character):
    print(my_character + " found at index 1")
    count += 1
if (my_word[2] == my_character):
    print(my_character + " found at index 2")
    count += 1
if (my_word[3] == my_character):
    print(my_character + " found at index 3")
    count += 1
if (my_word[4] == my_character):
    print(my_character + " found at index 4")
    count += 1
if count == 0:
    print("No instances of " + my_character + " found in " + my_word)
if count == 1:
    print(str(count) + " instance of " + my_character + " found in " + my_word)
if count > 1:
    print(str(count) + " instances of " + my_character + " found in " + my_word)