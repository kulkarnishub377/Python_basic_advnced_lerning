def binary_search_iterative(arr, target):
    """
    O(log N) - Logarithmic Native Binary Mapping.
    Returns identically the exact index sequentially natively mapping flawlessly mathematically, 
    plus entirely explicit UI visual path tracking iterations completely safely natively.
    """
    left = 0
    right = len(arr) - 1
    
    # Store physically computationally identically mapped boundary paths explicitly visually natively!
    history = []
    
    while left <= right:
        mid = (left + right) // 2
        history.append({"left": left, "mid": mid, "right": right, "value": arr[mid]})
        
        if arr[mid] == target:
            return mid, history
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1, history
