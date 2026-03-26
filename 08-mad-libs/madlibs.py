"""
Mad Libs Generator - Project 08
-------------------------------
What it does: Fill-in-the-blank storytelling. The program asks the player 
for nouns, verbs, adjectives, and adverbs, then inserts them into a funny 
story template. Includes multiple string templates stored as pure data.

Pro Hints:
- We use Python's `**kwargs` unpacking feature with `.format(**words)` 
  to inject dictionaries directly into string placeholders!
- This perfectly demonstrates separating data (the story templates) 
  from the logic (the input engine).
"""

# Storing templates externally from the logic keeps code clean
STORY_TEMPLATES = [
    "The {adjective} {animal} decided to {verb} over the {noun}.",
    "Did you know a {adjective} {noun} can {verb} faster than a {animal}?",
    "I was walking my {animal} when suddenly a {adjective} {noun} started to {verb}!"
]

def fill_story(template, user_words):
    """
    Injects a dictionary of user_words directly into the named placeholders.
    """
    return template.format(**user_words)

def play_mad_libs():
    print("Welcome to Mad Libs Generator!")
    print("Please provide the following words to create a story:\n")
    
    while True:
        # Ask for dynamic inputs
        words = {
            "adjective": input("Enter an adjective: ").strip(),
            "animal": input("Enter an animal: ").strip(),
            "verb": input("Enter a verb: ").strip(),
            "noun": input("Enter a noun: ").strip()
        }
        
        # Pick a story template at random (or prompt the user)
        # We will iterate through them for demonstration purposes,
        # but you could use random.choice()
        print("\nHere is your story:")
        print("-" * 40)
        
        import random
        template = random.choice(STORY_TEMPLATES)
        
        # Magic unpacked formatting
        story = fill_story(template, words)
        print(story)
        print("-" * 40)
        
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_mad_libs()
