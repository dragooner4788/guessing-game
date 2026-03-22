# About

This project is intended as a learning exercise for myself. I created this **Guessing Game** in order to practice and reinforce my Python skills.I wanted to start reinforcing my skills without relying on *Artificial Intelligence* assisting in creating the code. 

I have been using *Claude* to assist me with my learning but looking up why a *line* of code may not work, but I am not having it fix it for me, rather I am using it to assist me in understanding the code, and providing hint. 

## How Guessing Game Works

1. `my_number`: This is where we generate a random *Integer* between 1 and 10 for the *user* to guess.
2. `num_guess`: The user currently has **3** guesses. This is hard-coded currently.
3. `def guess_input()`: This function holds the logic for taking the *user* input and does some error handling:
  - Check to see if the input in a number using `ValueError`
  - Check to see if the user has input a number within range of 1 - 10
4. If the number the user input is **correct**, let them know. It will also break the loop.
5. If the number the user input is **incorrect** we will decrement `num_guess` and ask the user to try again. 

## Future Development

I will be iterating over the design of this program over time to reinforce my learning.
