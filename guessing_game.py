"""
1. Get a number to Guess
2. Give user 3 tries to Guess Number
3. If Guess = Number -- Player Wins, Else Player Loses
"""

import random

# Generates a number from 1 - 10 inclusive
my_number = random.randint(1, 10)
# print(my_number) -- for testing purposes.

# Set variable num_guesses to 3
# I want to make this a setting for the user in the future. For MVP we will use a hard-coded number.
num_guesses = 3


# I put the guess number funbctionality inside of a function so we can reuse it.
def guess_input():
    try:
        guess_number = int(input("Guess my Number (1 - 10): "))
        # We are checking to see if the number input by the user is within range. If it is not, we are providing them with the error message below.
        # I think there is an official way to do this, but for oour purposes, this is good enough.

        if (guess_number > 10) or (guess_number < 1):
            print(
                "Invalid Input: Provided number is out of range. Please enter a number from 1 - 10"
            )

    # Except is catching all input which is not an Integer. Even a float.
    # This is happening because we wrapped the input with int() to ensure that our input is an Integer.
    # If it is anything other than an Integer, we are catching it with `ValueError`
    except ValueError as e:
        print(f"Ivalid Input: {e}. Please enter a number.")

    return guess_number


while num_guesses > 0:
    user_guess = guess_input()
    if user_guess == my_number:
        print(f"You guessed my number! It was {my_number}.")
        break
    else:
        num_guesses -= 1  # This needs to go BEFORE the PRINT statement I do believe.
        print(
            f"That guess, {user_guess} is not my number.\nRemaining Guesses:{num_guesses}\nTry again!"
        )
