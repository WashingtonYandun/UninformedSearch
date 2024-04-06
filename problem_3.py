# Primero, definamos una clase de Grafo que use una matriz de adyacencia para su representación
# y luego implementemos la búsqueda BFS como una función externa.

class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]
        
    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight  # asumiendo que es un grafo no dirigido

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])
    
    def neighbors(self, node):
        return [idx for idx, presence in enumerate(self.matrix[node]) if presence != 0]

from typing import List, Tuple
from collections import deque

def bfs(graph: Graph, start: int, goal: int) -> Tuple[List[int], List[int]]:
    visited = [False] * graph.size
    queue = deque([start])
    visited[start] = True
    parent = [-1] * graph.size
    
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        
        for neighbor in graph.neighbors(current):
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)
    
    # Reconstruct the path from start to goal
    path = []
    current = goal
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    
    # Order of visitation
    order = [i for i in range(graph.size) if visited[i]]

    return order, path

# The given graph has 8 nodes. Let's create a graph of that size.
graph = Graph(8)

# Now let's add the edges. Nodes in the image are labeled A-G and S, but we will use 0-7
# S-A(6), S-B(4), S-C(2), A-D(3), B-D(4), B-E(9), C-E(1), D-F(5), D-E(2), E-H(5), G-E(8), G-H(8)

# Mapping of node letters to indices: A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, S=8
edges = [
    (7, 0, 6),  # S-A
    (7, 1, 4),  # S-B
    (7, 2, 2),  # S-C
    (0, 3, 3),  # A-D
    (1, 3, 4),  # B-D
    (1, 4, 9),  # B-E
    (2, 4, 1),  # C-E
    (3, 5, 5),  # D-F
    (3, 4, 2),  # D-E
    (4, 7, 5),  # E-H
    (6, 4, 8),  # G-E
    (6, 7, 8)   # G-H
]

# Add the edges to the graph
for u, v, weight in edges:
    graph.add_edge(u, v, weight)

# Let's do the BFS starting from S (7) to G (6)
bfs_order, bfs_path = bfs(graph, 7, 6)

bfs_order, bfs_path, graph.__str__()

