"""Structured Wordle."""

__author__ = "730664291"

GREEN_BOX = "\U0001F7E9"
WHITE_BOX = "\U00002B1C"
YELLOW_BOX = "\U0001F7E8"

def contains_char(word: str, chr: str) -> bool:
    """Checking if a character of secret word is located within the guess"""
    assert len(chr) == 1

    idx_count: int = 0

    while idx_count < len(word):
         if chr == word[idx_count]:
             return True
         else:
             idx_count += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Convert index info into emojis"""
    assert len(guess) == len(secret)
    str_stor = ""

    chr_count: int = 0

    while chr_count < len(secret):
        if guess[chr_count] == secret[chr_count]:
            str_stor += GREEN_BOX
        elif contains_char(secret, guess[chr_count]) is True:
            str_stor += YELLOW_BOX
        else:
            str_stor += WHITE_BOX
        chr_count += 1
    return str_stor

def input_guess(n: int) -> str:
    """The player's inputed guess."""
    my_guess: str = (input(f"Enter a { n } character word: "))
    while (len(my_guess) != n):
        my_guess = str(input(f"That wasn't { n } chars! Try again: "))
    return (str(my_guess))

def main() -> None:
    """The entrypoint of the program and main game loop."""

    secret = "codes"
    sec_length = len(secret)
    n_turns = 1
    won = False

    while n_turns <= 6 and won is False:
        print(f"=== Turn { n_turns }/6 ===")
        player_guess = (input_guess(sec_length))
        print(emojified(player_guess, secret))
        if player_guess == secret:
            won = True
        else:
            n_turns += 1
    if won is True:
        print(f"You won in {n_turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()