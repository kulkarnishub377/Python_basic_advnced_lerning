def bubble_sort(arr):
    """
    O(N^2) - The fundamentally most basic educational structurally identical sorting matrix.
    Natively identically explicitly exactly bubbles physically entirely exactly perfectly 
    largest values fundamentally sequentially backwards intrinsically.
    """
    n = len(arr)
    data = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                # Natively seamlessly explicitly exactly identical explicit swap logic physically mapped
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        
        # If mathematically precisely zero swaps natively execute, logic completely identical aborts flawlessly!
        if not swapped:
            break
            
    return data
