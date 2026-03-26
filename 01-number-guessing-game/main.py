"""
Number Guessing Game - Project 01
---------------------------------
What it does: The computer picks a secret random number between 1 and 100.
The player guesses repeatedly, and the program responds with 'Too high' or 'Too low' 
hints until the player wins. Tracks the number of attempts.

Pro Hints:
- We use try-except to handle cases where the user types letters instead of a number.
- We use a while loop that only breaks when the correct number is guessed.
"""

import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a secret number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    # Generate the secret number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    # Enter an infinite loop until the correct guess is made
    while True:
        user_input = input("Enter your guess (or 'q' to quit): ")
        
        # Allow the user to gracefully exit
        if user_input.lower() == 'q':
            print(f"Thanks for playing! The secret number was {secret_number}.")
            break
            
        # Input Validation: Ensure the user typed a valid integer
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            continue  # Skip the rest of the loop and prompt again
            
        attempts += 1
        
        # Logic to check the guess against the secret number
        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts to win.\n")
            break  # Break out of the loop, ending the game

if __name__ == "__main__":
    play_game()
