import time
import random

def constant_time_o_1(data):
    """O(1) - Retrieves the specifically first item inherently instantly."""
    if not data: return None
    time.sleep(0.001) # Simulated physical delay
    return data[0]

def linear_time_o_n(data):
    """O(N) - Iterates dynamically across every parameter unconditionally."""
    total = 0
    for item in data:
        time.sleep(0.0001)
        total += item
    return total

def quadratic_time_o_n2(data):
    """O(N^2) - Natively nested loops generating massive computational scaling operations."""
    count = 0
    # To prevent UI freeze, we limit physical mathematical data sizes natively
    limit = min(len(data), 500)
    subset = data[:limit]
    
    for i in subset:
        for j in subset:
            time.sleep(0.00001)
            count += 1
    return count
