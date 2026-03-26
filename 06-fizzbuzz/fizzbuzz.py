"""
FizzBuzz - Project 06
---------------------
What it does: The classic interview warm-up. Prints numbers 1-100, replacing 
multiples of 3 with Fizz, multiples of 5 with Buzz, and multiples of both with FizzBuzz. 
Extended with configurable range and custom words.

Pro Hints:
- Ordering of conditions matters! We check for `i % (fizz*buzz) == 0` first.
- Default function parameters allow `fizzbuzz(15)` to work out-of-the-box, 
  but also `fizzbuzz(20, fizz=2, buzz=7)` to change the logic easily.
- No emojis are hardcoded to keep the logic completely pure.
"""

def fizzbuzz(n, fizz=3, buzz=5):
    """
    Executes the FizzBuzz logic up to number 'n'.
    fizz and buzz can be overridden to check different multiples.
    """
    print(f"Running FizzBuzz up to {n} (Fizz={fizz}, Buzz={buzz}):")
    print("-" * 30)
    
    for i in range(1, n + 1):
        # We must check the combined multiple FIRST!
        # If we checked 3 first, 15 would print "Fizz" and skip "FizzBuzz".
        if i % (fizz * buzz) == 0:
            print("FizzBuzz")
        elif i % fizz == 0:
            print("Fizz")
        elif i % buzz == 0:
            print("Buzz")
        else:
            print(i)
            
    print("-" * 30)

if __name__ == "__main__":
    # Standard 1-100 FizzBuzz
    fizzbuzz(100)
    
    # Custom 1-20 FizzBuzz where multiples of 2 are "Fizz" and 4 are "Buzz"
    # fizzbuzz(20, fizz=2, buzz=4)
