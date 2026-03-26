"""
Rock Paper Scissors - Project 07
--------------------------------
What it does: Play Rock Paper Scissors against the computer with full score 
tracking across multiple rounds. Win/lose/draw logic is stored in a dictionary, 
making it extremely concise and easy to extend.

Pro Hints:
- Instead of writing 9 `if/elif` statements, we map the winning moves in a dictionary.
- We track ties, wins, and losses in a state dictionary to output a scoreboard.
"""

import random

def play_rps():
    # Store rules dynamically. The Key is the shape, the Value is what it BEATS.
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    # Track the ongoing session score
    scoreboard = {"player": 0, "computer": 0, "ties": 0}
    choices = list(wins.keys())
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', 'scissors' or 'q' to quit.\n")
    
    while True:
        player = input("Your move: ").strip().lower()
        
        if player == 'q':
            print("\nFinal Scoreboard:")
            print(f"Wins: {scoreboard['player']} | Losses: {scoreboard['computer']} | Ties: {scoreboard['ties']}")
            print("Thanks for playing!")
            break
            
        if player not in choices:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue
            
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        
        # Determine outcome using our dictionary logic!
        if player == computer:
            print("Result: It's a tie!\n")
            scoreboard["ties"] += 1
        elif wins[player] == computer:
            print("Result: You win this round!\n")
            scoreboard["player"] += 1
        else:
            print("Result: You lose this round.\n")
            scoreboard["computer"] += 1

if __name__ == "__main__":
    play_rps()
