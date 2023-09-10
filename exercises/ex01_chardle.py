"""EX01 - Chardle - A cute step toward Worldle"""

__author__ = 730664291

my_five_letter_word = input("Enter a 5-character word: ")

if (len(my_five_letter_word) != 5):
    print("Error: Word must contain 5 characters")
    exit(len(my_five_letter_word) != 5)

my_single_character = input("Enter a single character: ")

if (len(my_single_character) != 1):
    print("Error: Character must be a single character.")
    exit(len(my_five_letter_word) != 1)

characters_found = int == 0

print("Searching for " + my_single_character + " in " + my_five_letter_word)

if (my_five_letter_word[0] == my_single_character):
    print(my_single_character + " found at index 0")
    characters_found += 1
if (my_five_letter_word[1] == my_single_character):
    print(my_single_character + " found at index 1")
    characters_found += 1
if (my_five_letter_word[2] == my_single_character):
    print(my_single_character + " found at index 2")
    characters_found += 1
if (my_five_letter_word[3] == my_single_character):
    print(my_single_character + " found at index 3")
    characters_found += 1
if (my_five_letter_word[4] == my_single_character):
    print(my_single_character + " found at index 4")
    characters_found += 1
if characters_found == 0:
    print("No instances of " + my_single_character + " found in " + my_five_letter_word)
if characters_found == 1:
    print(str(characters_found) + " instance of " + my_single_character + " found in " + my_five_letter_word)
if characters_found > 1:
    print(str(characters_found) + " instances of " + my_single_character + " found in " + my_five_letter_word)


