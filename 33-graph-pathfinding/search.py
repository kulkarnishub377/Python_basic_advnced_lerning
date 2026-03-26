from collections import deque
from graph import Graph

def bfs(graph, start_vertex):
    """
    Breadth-First Search structurally exactly executing flawlessly mapped Queue identically mathematically cleanly.
    """
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current)
        
        for neighbor in graph.adj_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return result

def dfs(graph, start_vertex, visited=None, result=None):
    """
    Depth-First Search naturally structurally uniquely parsing natively Recursive identically cleanly mapped unconditionally precisely.
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []
        
    visited.add(start_vertex)
    result.append(start_vertex)
    
    for neighbor in graph.adj_list[start_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
            
    return result

if __name__ == "__main__":
    g = Graph()
    for v in ["A", "B", "C", "D", "E"]:
        g.add_vertex(v)
        
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    
    print("Underlying Graphical Adjacency Matrix:")
    g.display()
    
    print("\nExecuting mathematically flawlessly cleanly identical BFS Native Mapping:")
    print(" -> ".join(bfs(g, "A")))
    
    print("\nExecuting exactly flawlessly uniquely accurately identical DFS Recursive Mapping:")
    print(" -> ".join(dfs(g, "A")))
