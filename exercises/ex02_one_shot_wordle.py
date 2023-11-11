"""Creating a One-Shot Wordle."""

__author__ = "730664291"

secret = "python"

secret_len = len(secret)

my_guess = input(f"What is your { secret_len }-letter guess? ")

while len(str(my_guess)) != len(str(secret)):
    my_guess = input(f"That was not { secret_len } letters! Try again: ")

character_idx: int = 0

str_store = ""

exists_else = False

idx_check: int = 0

while character_idx <= (secret_len - 1):
    if secret[character_idx] == my_guess[character_idx]:
        str_store += ("\U0001F7E9")
        character_idx += 1
    elif secret[character_idx] != my_guess[character_idx]:
        while (exists_else is False) and idx_check <= (secret_len - 1):
            if secret[idx_check] == my_guess[character_idx]:
                exists_else = True
            else:
                idx_check += 1
        if exists_else is False:
            str_store += ("\U00002B1C")
            character_idx += 1
            idx_check -= idx_check
        elif exists_else is True:
            str_store += ("\U0001F7E8")
            character_idx += 1
            exists_else = False
            idx_check -= idx_check


print(str_store)

if my_guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")