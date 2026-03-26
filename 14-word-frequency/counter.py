"""
Word Frequency Counter - Project 14
-----------------------------------
What it does: Reads any text file, standardizes the capitalization, cleanly 
strips complicated punctuation utilizing the `re` (regex) library, and counts 
the N most common words cleanly leveraging the `collections.Counter` module. 
Finally, output is charted into a terminal-based bar graph natively.

Pro Hints:
- We completely avoid writing a messy dictionary loop for counting! 
  `collections.Counter()` is written in C under the hood and drastically speeds up tallying!
- `re.findall(r"[a-z]+", text)` provides highly optimized word boundary extraction.
"""

from collections import Counter
import re
import os

def analyze_document(path, top_n=5):
    """
    Reads a document, produces a clean tally of tokens, and prints a chart.
    """
    if not os.path.exists(path):
        print(f"Error: Unable to locate {path}")
        return

    # Read data sequentially and force normalize to purely lowercase letters
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()
        
    # Extract only strictly matched alphabetical words, entirely discarding punctuation spaces
    words = re.findall(r"[a-z]+", text)
    
    # Feed resulting pure word array natively into the C-optimized Python Counter class
    word_tally = Counter(words)
    
    print(f"Total Words Scanned: {len(words)}")
    print(f"Unique Words Found: {len(word_tally)}")
    print(f"\nTop {top_n} Most Frequent Words:")
    print("-" * 35)

    # Use .most_common() which natively sorts the dictionary automatically
    for word, count in word_tally.most_common(top_n):
        # We manually render a simple text-based bar chart using string multipliers
        bar = "#" * count
        print(f"{word:<12} | {count:>3} | {bar}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_file = os.path.join(current_dir, "sample.txt")
    
    # Requesting analysis for the top 5 ranking matches against our arbitrary text
    analyze_document(sample_file, top_n=5)
