"""
Title: Guessing Game
Decription: A game where the user has to guess a number.
Date: 3-2-2026
Author: Guy Friley
"""
import random

# 1. Set a number for the user to guess.
# 2. Define number of guesses
# 2a. Ask the user if they want to define the number of guesses.
# If YES: Set number of guesses to the input
# If NO: Default to 3 guesses.
# 3. Ask the user to guess for number of guesses defined
# 4. If the user guesses the number, let them know.
# 5. If they run out of guesses, let them know

# Define Number of Guesses Function guess_prompt

def get_num_guesses():
    while True:
        get_num_guess_prompt = input("How many guesses would you like: ")
        #print(num_guess_value)
        try:
            num_guess_value = int(get_num_guess_prompt)
            if num_guess_value > 0:
                return num_guess_value
            break
        # I don't think we even hit this except block.
        except ValueError as e:
            print(f"Invalid Input: {e}")

# Define Number of Guesses Function

def set_num_guesses():
    while True:
        guess_prompt = input("Would you like to set a custom number of guesses? (y/n): ")
        guess_prompt.lower()
        print(guess_prompt)
        try:
            if guess_prompt == 'y':
                #print("YES BLOCK")
                num_guesses_set = get_num_guesses()
                num_guesses = num_guesses_set
                return num_guesses
                break
            if guess_prompt == 'n':
                #print("NO BLOCK")
                #print(num_guesses)
                num_guesses = 3
                return num_guesses
                break
        except ValueError as e:
            print(f"Please input a valid number! Error: {e}")

# Set Guess Input fo User

def guess_input():
    try:
        guess_number = int(input("Guess my Number (1 - 10): "))
        # We are checking to see if the number input by the user is within range. If it is not, we are providing them with the error message below.
        # I think there is an official way to do this, but for oour purposes, this is good enough.

        if guess_number != None and guess_number != "":
            return guess_number
    # Except is catching all input which is not an Integer. Even a float.
    # This is happening because we wrapped the input with int() to ensure that our input is an Integer.
    # If it is anything other than an Integer, we are catching it with `ValueError`
    except ValueError as e:
        print(f"Ivalid Input: {e}. Please enter a number.")

    #return guess_number

# Set a number for the User to Guessing
# Define variable as a constant.
SECRET_NUMBER_GUESS = random.randint(1,10)

num_guesses = set_num_guesses()

# RUNNING THE GAME
# set_num_guesses()
while num_guesses > 0:

    user_guess = guess_input()
    if user_guess is None:
        continue
    if (user_guess > 10) or (user_guess < 1):
        print("Invalid Input: Number entered is not between 1 - 10!")
        continue
    if user_guess == SECRET_NUMBER_GUESS:
        print(f"You guessed my number! It was {SECRET_NUMBER_GUESS}.")
        break
    else:
        num_guesses -= 1  # This needs to go BEFORE the PRINT statement I do believe.
        print(
            f"That guess, {user_guess} is not my number.\nRemaining Guesses:{num_guesses}\nTry again!"
        )
