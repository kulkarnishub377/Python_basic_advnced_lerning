"""
Palindrome Checker - Project 05
-------------------------------
What it does: Checks if a word or full sentence is a palindrome. Strips spaces and 
punctuation, normalizes to lowercase, and compares the string to its reverse structure.

Pro Hints:
- `[::-1]` is Python's highly optimized slice trick for reversing arrays/strings.
- Cleaning strings heavily before algorithmic comparison ensures "A nut for a jar of tuna." 
  is still identified as a palindrome gracefully. 
"""

import string

def clean_string(text):
    """
    Strips spaces and punctuation, returning pure lowercase letters.
    """
    # Create a translation table to remove all punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Lowercase, remove spaces, and map punctuation away
    cleaned = text.lower().replace(" ", "").translate(translator)
    return cleaned

def is_palindrome(text):
    """
    Returns True if the cleaned text matches its reverse, False otherwise.
    """
    cleaned = clean_string(text)
    
    # Optimization: empty strings aren't generally handled as valid input types in games
    if not cleaned: 
        return False
        
    # Return evaluation of array sliced backwards against standard
    return cleaned == cleaned[::-1]

def checker():
    print("Welcome to the Palindrome Checker!")
    print("A palindrome is a word or phrase that reads the same forwards and backwards.")
    
    while True:
        phrase = input("\nEnter a word/phrase (or 'q' to quit): ")
        
        if phrase.lower() == 'q':
            print("Goodbye!")
            break
            
        if is_palindrome(phrase):
            print(f"YES, '{phrase}' is a palindrome!")
        else:
            print(f"NO, '{phrase}' is NOT a palindrome.")

if __name__ == "__main__":
    checker()
