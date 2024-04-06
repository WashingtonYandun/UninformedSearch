from collections import deque
import heapq

class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex][to_vertex] = weight
        if not self.directed:
            self.graph[to_vertex][from_vertex] = weight

    def get_neighbors(self, vertex):
        return self.graph[vertex]

    def get_vertices(self):
        return list(self.graph.keys())
    
    def __str__(self):
        # print the graph as a dictionary
        return str(self.graph)

# Create the graph based on the given diagram
g = Graph()
edges = [
    ('S', 'A', 3), ('S', 'B', 6), ('S', 'C', 2),
    ('A', 'D', 3),
    ('B', 'D', 4), ('B', 'E', 9), ('B', 'G', 5),
    ('C', 'E', 2),
    ('D', 'F', 5),
    ('E', 'H', 5),
    ('F', 'G', 6),
    ('G', 'H', 8)
]

# Adding edges to the graph
for edge in edges:
    g.add_edge(*edge)

# Breadth-First Search (BFS)
def bfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the starting node
    parents = {start: None}  # Keep track of the parents of the nodes
    
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        
        if vertex == goal:
            break
        
        for neighbor in sorted(graph.get_neighbors(vertex)):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                queue.append(neighbor)
                
    # Reconstruct the path from start to goal
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()  # The path is constructed in reverse
    return visited, path

# Depth-First Search (DFS)
def dfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    stack = [start]  # Initialize a stack with the starting node
    parents = {start: None}  # Keep track of the parents of the nodes
    
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        
        if vertex == goal:
            break
        
        for neighbor in sorted(graph.get_neighbors(vertex), reverse=True):
            if neighbor not in visited:
                parents[neighbor] = vertex
                stack.append(neighbor)
                
    # Reconstruct the path from start to goal
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()  # The path is constructed in reverse
    return visited, path

# Uniform-Cost Search (UCS)
def ucs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    queue = [(0, start)]  # Initialize a priority queue with the starting node
    parents = {start: None}  # Keep track of the parents of the nodes
    costs = {start: 0}  # Keep track of the costs of the nodes
    
    while queue:
        cost, vertex = heapq.heappop(queue)
        visited.add(vertex)
        
        if vertex == goal:
            break
        
        for neighbor, weight in graph.get_neighbors(vertex).items():
            if neighbor not in visited:
                new_cost = cost + weight
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    parents[neighbor] = vertex
                    heapq.heappush(queue, (new_cost, neighbor))
                    
    # Reconstruct the path from start to goal
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()  # The path is constructed in reverse
    return visited, path, costs[goal]

# Perform searches
bfs_visited, bfs_path = bfs(g, 'S', 'G')
dfs_visited, dfs_path = dfs(g, 'S', 'G')
ucs_visited, ucs_path, ucs_cost = ucs(g, 'S', 'G')

print(bfs_visited, bfs_path,"\n")
print(dfs_visited, dfs_path,"\n")
print(ucs_visited, ucs_path, ucs_cost,"\n")