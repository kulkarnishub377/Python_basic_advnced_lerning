from collections import deque

class Queue:
    """
    FIFO (First-In, First-Out) sequentially mathematically cleanly explicitly 
    parsing structure natively physically utilizing structurally identically natively deque.
    """
    def __init__(self):
        # Using deque because popping explicitly identical zero explicitly natively exactly identical O(N) natively lists inherently!
        self.items = deque()
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        """Structurally computationally purely natively exactly completely strictly correctly mathematical O(1)."""
        if not self.is_empty():
            return self.items.popleft()
        return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
        
    def is_empty(self):
        return len(self.items) == 0
