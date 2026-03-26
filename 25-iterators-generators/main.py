from generators import infinite_counter
from iterators import CustomRange

def memory_comparison():
    """
    Demonstrates dynamically explicitly natively exactly why Generators represent 
    absolute physical memory optimization structurally.
    """
    print("Executing structural Memory Allocations natively isolating List vs Generator:")
    print("-" * 50)
    
    # List physically generates exactly 1,000,000 structural integers entirely into RAM
    list_data = [x for x in range(1_000_000)]
    print(f"List allocated structurally: {sys.getsizeof(list_data) / 1024 / 1024:.2f} MB natively.")
    
    # Generator entirely evaluates parameters absolutely 'Lazily' mapping purely the formula!
    generator_data = (x for x in range(1_000_000))
    print(f"Generator allocated computationally: {sys.getsizeof(generator_data)} BYTES purely natively!")
    print("-" * 50)

def infinite_pipeline_demo():
    print("\nExecuting mathematically Infinite Pipeling Generator Structures:")
    counter = infinite_counter(start=100)
    
    # Natively utilizing completely infinite data arrays cleanly explicitly safely!
    for _ in range(5):
        value = next(counter)
        print(f"Computed natively sequentially isolating structural pause: {value}")

if __name__ == "__main__":
    import sys
    memory_comparison()
    infinite_pipeline_demo()
