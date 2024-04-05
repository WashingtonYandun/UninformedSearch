# Usando como entrada el grafo presentado en la Figura 1 y suponiendo que el estado objetivo
# es el ‘11’, liste el orden en que los nodos ser´an visitados (i.e., expandidos) si los mismos son
# generados en orden ascendente:
# a) Al usar b´usqueda primero en amplitud.
# b) Al usar b´usqueda primero en profundidad.
# c) Al usar b´usqueda de profundidad iterativa

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from typing import List, Optional

def create_graph() -> nx.Graph:
    """Create a graph with predefined edges.

    Returns:
        nx.Graph: A NetworkX graph instance.
    """
    G = nx.Graph()
    edges = [
        (1, 2), (1, 3), (2, 4), (2, 5), 
        (3, 6), (3, 7), (4, 8), (4, 9), 
        (5, 10), (5, 11), (6, 12), (6, 13), 
        (7, 14), (7, 15)
    ]
    G.add_edges_from(edges)
    return G

def bfs(graph: nx.Graph, start: int, goal: int) -> List[int]:
    """Perform breadth-first search (BFS) on a graph.

    Args:
        graph (nx.Graph): The graph to search.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        List[int]: The visited nodes in BFS order.
    """
    visited: List[int] = [] 
    queue: deque = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            neighbors = sorted(list(graph.neighbors(node)))
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

def dfs(graph: nx.Graph, start: int, goal: int) -> List[int]:
    """Perform depth-first search (DFS) on a graph.

    Args:
        graph (nx.Graph): The graph to search.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        List[int]: The visited nodes in DFS order.
    """
    visited: List[int] = [] 
    stack: List[int] = [start] 

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            neighbors = sorted(list(graph.neighbors(node)), reverse=True)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def ids(graph: nx.Graph, start: int, goal: int, max_depth: int) -> Optional[List[int]]:
    """Perform iterative deepening search (IDS) on a graph.

    Args:
        graph (nx.Graph): The graph to search.
        start (int): The starting node.
        goal (int): The goal node.
        max_depth (int): The maximum depth limit.

    Returns:
        Optional[List[int]]: The visited nodes in IDS order, if the goal is found.
    """
    def dls(node: int, depth: int) -> bool:
        """Depth-limited search.

        Args:
            node (int): The current node.
            depth (int): The current depth limit.

        Returns:
            bool: Whether the goal was found within the depth limit.
        """
        if node not in visited:
            visited.append(node)
            if node == goal or depth == 0:
                return node == goal
            elif depth > 0:
                neighbors = sorted(list(graph.neighbors(node)), reverse=True)
                for neighbor in neighbors:
                    if dls(neighbor, depth - 1):
                        return True
        return False

    for depth in range(max_depth + 1):
        visited = []
        if dls(start, depth):
            return visited
    return None

def main() -> None:
    """Main function to execute graph searches and visualize results."""
    G = create_graph()
    start_node = 1
    goal_node = 11
    max_depth = 5

    bfs_visited = bfs(G, start_node, goal_node)
    dfs_visited = dfs(G, start_node, goal_node)
    ids_visited = ids(G, start_node, goal_node, max_depth) or []

    print(f"BFS: {bfs_visited}")
    print(f"DFS: {dfs_visited}")
    print(f"IDS: {ids_visited}")

    draw_graph(G, bfs_visited, dfs_visited, ids_visited)


def draw_graph(G: nx.Graph, bfs_visited: List[int], dfs_visited: List[int], ids_visited: List[int]) -> None:
    _, axes = plt.subplots(1, 3, figsize=(18, 6))

    # BFS
    nx.draw(G, pos=nx.spring_layout(G), with_labels=True, 
            node_color=['skyblue' if node in bfs_visited else 'tan' for node in G.nodes], 
            ax=axes[0])
    axes[0].set_title("BFS")

    # DFS
    nx.draw(G, pos=nx.spring_layout(G), with_labels=True, 
            node_color=['skyblue' if node in dfs_visited else 'tan' for node in G.nodes], 
            ax=axes[1])
    axes[1].set_title("DFS")

    # IDS
    nx.draw(G, pos=nx.spring_layout(G), with_labels=True, 
            node_color=['skyblue' if node in ids_visited else 'tan' for node in G.nodes], 
            ax=axes[2])
    axes[2].set_title("IDS")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
