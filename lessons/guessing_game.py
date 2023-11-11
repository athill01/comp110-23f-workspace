"""Program That Loops Until Correct Number Is Guessed."""

from random import randint
secret: int = randint(1, 10)
guess: int = int(input("Guess a number between 1 and 10: "))
if guess > 10:
    print("That ain't a valid number homie")
    guess = input("Try again")


guess_count = 0
max_guess: int = 3

while (guess != secret) and (guess_count < (max_guess - 1)):
    print("Wrong!")
    # If guess is too low, tell them
    if guess < secret:
        print("Too low!")
    # If guess is too high, tell them
    else:
        print("Too high!")
    # Ask for a different guess
    guess = int(input("Guess again: "))
    guess_count += 1

# If I've reaced this point, guess == secret
if guess == secret:
    print("You guessed correctly!")
else:
    print("You lose!!!")
