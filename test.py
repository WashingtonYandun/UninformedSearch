import matplotlib.pyplot as plt
import networkx as nx
from typing import Dict, Tuple, List

edges = {
    ('S', 'A'): 3,
    ('S', 'B'): 6,
    ('S', 'C'): 2,
    ('A', 'D'): 3,
    ('B', 'D'): 4,
    ('B', 'E'): 9,
    ('C', 'E'): 2,
    ('D', 'F'): 5,
    ('E', 'H'): 5,
    ('F', 'G'): 5,
    ('G', 'H'): 8,
}

# Create a directed graph
G = nx.Graph()
G.add_weighted_edges_from([(u, v, w) for (u, v), w in edges.items()])

# Define BFS, DFS, and UCS functions

def bfs(graph: nx.Graph, start: str, goal: str) -> Tuple[List[str], List[str]]:
    visited = []  # List to keep track of visited nodes.
    queue = []     # Initialize a queue
    parent_map = {}

    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        if m == goal:
            break
        for neighbor in sorted(list(graph.neighbors(m))):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                parent_map[neighbor] = m
    
    # Trace back the path from goal to start
    path = [goal]
    while path[-1] != start:
        path.append(parent_map[path[-1]])
    path.reverse()
    
    return visited, path

def dfs(graph: nx.Graph, start: str, goal: str) -> Tuple[List[str], List[str]]:
    visited = []  # List to keep track of visited nodes.
    stack = []     # Initialize a stack
    parent_map = {}

    stack.append(start)

    while stack:
        m = stack.pop()
        if m not in visited:
            visited.append(m)
            if m == goal:
                break
            for neighbor in sorted(list(graph.neighbors(m)), reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)
                    parent_map[neighbor] = m
    
    # Trace back the path from goal to start
    path = [goal]
    while path[-1] != start:
        path.append(parent_map[path[-1]])
    path.reverse()
    
    return visited, path

def ucs(graph: nx.Graph, start: str, goal: str) -> Tuple[List[str], List[str]]:
    visited = []  # List to keep track of visited nodes.
    queue = []     # Initialize a priority queue
    parent_map = {}
    cost_map = {start: 0}

    queue.append((0, start))

    while queue:
        queue.sort(key=lambda x: x[0])  # Sort the queue based on the cost
        cost, m = queue.pop(0)
        if m not in visited:
            visited.append(m)
            if m == goal:
                break
            for neighbor in graph.neighbors(m):
                if neighbor not in visited:
                    total_cost = cost + graph[m][neighbor]['weight']
                    if neighbor not in cost_map or total_cost < cost_map[neighbor]:
                        queue.append((total_cost, neighbor))
                        parent_map[neighbor] = m
                        cost_map[neighbor] = total_cost
    
    # Trace back the path from goal to start
    path = [goal]
    while path[-1] != start:
        path.append(parent_map[path[-1]])
    path.reverse()
    
    return visited, path

# Execute each search strategy
bfs_visited, bfs_path = bfs(G, 'S', 'G')
dfs_visited, dfs_path = dfs(G, 'S', 'G')
ucs_visited, ucs_path = ucs(G, 'S', 'G')

print(bfs_visited, bfs_path, "\n")
print(dfs_visited, dfs_path, "\n")
print(ucs_visited, ucs_path, "\n")
