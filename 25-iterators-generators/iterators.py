class CustomRange:
    """
    A purely structural native Python Class explicitly modeling 
    exactly how Iterators mathematically function internally!
    """

    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        """
        Dunder __iter__ strictly returns the physical Iterator Object itself 
        (which is `self` natively because we constructed `__next__` below!).
        """
        return self

    def __next__(self):
        """
        Dunder __next__ defines exactly what structural value generates continuously.
        Crucially, it MUST explicitly throw `StopIteration` resolving loops completely cleanly!
        """
        if self.current >= self.end:
            raise StopIteration
            
        value = self.current
        self.current += self.step
        return value

def demonstrate_iterator():
    print("Testing the purely structural CustomRange Class natively:")
    
    # We natively iterate our physically mapped Class seamlessly!
    for num in CustomRange(0, 10, 2):
        print(f"Generated natively: {num}")

if __name__ == "__main__":
    demonstrate_iterator()
