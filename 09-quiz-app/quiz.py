"""
Basic Quiz App - Project 09
---------------------------
What it does: A multiple-choice quiz engine. Questions and answers are stored 
as a list of dictionaries. The app loops through each question, validates input, 
scores the answer, and shows a final percentage at the end.

Pro Hints:
- We import `QUESTIONS` from a separate file (`questions.py`) to keep the logic clean.
- We use `.upper()` to process user inputs securely (A, B, C, D).
- `sum()` with a generator expression is a pro-level Pythonic way to score tests!
"""

from questions import QUESTIONS

def ask_question(q_dict):
    """
    Displays the question and options. Parses the user's choice.
    Returns True if correct, False otherwise.
    """
    print(f"\nQ: {q_dict['question']}")
    
    # Dynamically generate letters A, B, C, D for the options
    letters = ['A', 'B', 'C', 'D']
    for idx, opt in enumerate(q_dict['options']):
        print(f"   {letters[idx]}) {opt}")
        
    while True:
        choice = input("Your answer (A/B/C/D): ").strip().upper()
        if choice in letters:
            # Map choice back to the index (A -> 0, B -> 1 ...)
            chosen_index = letters.index(choice)
            chosen_answer = q_dict['options'][chosen_index]
            
            # Case-insensitive string comparison for safety
            if chosen_answer.lower() == q_dict['answer'].lower():
                print("Correct!")
                return True
            else:
                print(f"Wrong! The correct answer was {q_dict['answer']}.")
                return False
        else:
            print("Invalid input! Please choose A, B, C, or D.")

def run_quiz():
    print("Welcome to the Ultimate Knowledge Quiz!")
    print(f"There are {len(QUESTIONS)} questions in total.\n")
    
    # Calculate score using a generator
    # For each question, it calls ask_question() and adds 1 if it returns True
    score = sum(1 for q in QUESTIONS if ask_question(q))
    
    # Percentage calculation
    percentage = (score / len(QUESTIONS)) * 100
    
    print("\n" + "=" * 30)
    print(f"Quiz Complete! You scored {score}/{len(QUESTIONS)}")
    print(f"Final Grade: {percentage:.1f}%")
    print("=" * 30)

if __name__ == "__main__":
    run_quiz()
