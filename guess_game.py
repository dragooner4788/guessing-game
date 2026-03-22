"""
Let's objectify our code!
"""

import random

class GuessingGame:

    def __init__(self, num_guesses=3):
        self.num_guesses = num_guesses
        self.SECRET_NUMBER_GUESS = self.create_secret_number_guess()

    def create_secret_number_guess(self):
        return random.randint(1,10)

    def print_secret_number(self):
        print(self.SECRET_NUMBER_GUESS)

    def get_secret_number(self):
        return self.SECRET_NUMBER_GUESS

    def get_num_guesses(self):
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

    def set_num_guesses(self):
        while True:
            guess_prompt = input("Would you like to set a custom number of guesses? (y/n): ")
            guess_prompt = guess_prompt.lower()
            print(guess_prompt)
            try:
                if guess_prompt == 'y':
                    num_guesses_set = self.get_num_guesses()
                    num_guesses = num_guesses_set
                    self.num_guesses = num_guesses
                    break
                if guess_prompt == 'n':
                    self.num_guesses = 3
                    break
            except ValueError as e:
                print(f"Please input a valid number! Error: {e}")
    def guess_input(self):
        try:
            guess_number = int(input("Guess my Number (1 - 10): "))
            # We are checking to see if the number input by the user is within range. If it is not, we are providing them with the error message below.
            # I think there is an official way to do this, but for oour purposes, this is good enough.
            return guess_number
        # Except is catching all input which is not an Integer. Even a float.
        # This is happening because we wrapped the input with int() to ensure that our input is an Integer.
        # If it is anything other than an Integer, we are catching it with `ValueError`
        except ValueError as e:
            print(f"Ivalid Input: {e}. Please enter a number.")
    def play(self):
        # Ask for number of guesses
        self.set_num_guesses()
        # RUNNING THE GAME
        # set_num_guesses()
        while self.num_guesses > 0:
            user_guess = self.guess_input()
            if user_guess is None:
                continue
            if (user_guess > 10) or (user_guess < 1):
                print("Invalid Input: Number entered is not between 1 - 10!")
                continue
            if user_guess == self.SECRET_NUMBER_GUESS:
                print(f"You guessed my number! It was {self.SECRET_NUMBER_GUESS}.")
                break
            else:
                self.num_guesses -= 1  # This needs to go BEFORE the PRINT statement I do believe.
                print(
                    f"That guess, {user_guess} is not my number.\nRemaining Guesses:{self.num_guesses}\nTry again!"
                )
        if self.num_guesses == 0:
            print(f"You lost! My secret number is {self.get_secret_number()}")
my_game = GuessingGame().play()
