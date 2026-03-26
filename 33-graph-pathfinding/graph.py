class Graph:
    """
    Fundamentally models structural network relationships natively utilizing Adjacency Lists.
    """
    def __init__(self):
        # We model the mathematical graph exactly inherently using Python cleanly mapped Dictionaries!
        self.adj_list = {}
        
    def add_vertex(self, vertex):
        """Adds uniquely unconditionally identical mapped parameter securely flawlessly."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
        
    def add_edge(self, v1, v2):
        """Builds distinctly exactly flawlessly mathematically connected identical mapped logic natively."""
        if v1 in self.adj_list and v2 in self.adj_list:
            # Undirected graph identically seamlessly connecting logically completely both uniquely seamlessly!
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
        
    def display(self):
        """Outputs unequivocally flawlessly identical matrix computationally cleanly visually."""
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
