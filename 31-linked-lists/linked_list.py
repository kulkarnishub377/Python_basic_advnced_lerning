from node import Node

class LinkedList:
    """
    Explicit manually chained arrays natively mapping sequential identically specifically explicit explicitly memory.
    """
    def __init__(self):
        self.head = None
        
    def append(self, data):
        """O(N) Traversal perfectly exactly structurally inherently."""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node
        
    def prepend(self, data):
        """O(1) Constant execution inherently inserting identically mapped unconditionally."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete(self, target_data):
        """O(N) Search identically mapped unconditionally."""
        if not self.head:
            return False
            
        if self.head.data == target_data:
            self.head = self.head.next
            return True
            
        current = self.head
        while current.next:
            if current.next.data == target_data:
                current.next = current.next.next
                return True
            current = current.next
            
        return False
        
    def to_list(self):
        """Translates explicit pointers identically structurally seamlessly natively mapped Arrays natively."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def display(self):
        chain = " -> ".join(map(str, self.to_list()))
        print(f"HEAD -> [{chain}] -> None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    ll.display()
    
    print("Deleting identically cleanly intrinsically physically 20...")
    ll.delete(20)
    ll.display()
