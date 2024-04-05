from collections import deque
from typing import Dict, List, Optional

def create_graph_dict() -> Dict[int, List[int]]:
    """Create a graph with predefined edges using a dictionary.

    Returns:
        Dict[int, List[int]]: A dictionary representing the graph.
    """
    edges: Dict[int, List[int]] = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [8, 9],
        5: [10, 11],
        6: [12, 13],
        7: [14, 15],
        8: [], 9: [], 10: [], 11: [],
        12: [], 13: [], 14: [], 15: []
    }
    return edges

def bfs_dict(graph: Dict[int, List[int]], start: int, goal: int) -> List[int]:
    """Perform breadth-first search (BFS) using a dictionary-based graph representation.

    Args:
        graph (Dict[int, List[int]]): The graph to search.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        List[int]: The visited nodes in BFS order.
    """
    visited: List[int] = []
    queue: deque[int] = deque([start])

    while queue:
        node: int = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            for neighbor in sorted(graph[node]):
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

def dfs_dict(graph: Dict[int, List[int]], start: int, goal: int) -> List[int]:
    """Perform depth-first search (DFS) using a dictionary-based graph representation.

    Args:
        graph (Dict[int, List[int]]): The graph to search.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        List[int]: The visited nodes in DFS order.
    """
    visited: List[int] = []
    stack: List[int] = [start]

    while stack:
        node: int = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def ids_dict(graph: Dict[int, List[int]], start: int, goal: int, max_depth: int) -> Optional[List[int]]:
    """Perform iterative deepening search (IDS) using a dictionary-based graph representation.

    Args:
        graph (Dict[int, List[int]]): The graph to search.
        start (int): The starting node.
        goal (int): The goal node.
        max_depth (int): The maximum depth to search.

    Returns:
        Optional[List[int]]: The visited nodes in IDS order, if found.
    """
    def dls_dict(node: int, depth: int) -> bool:
        """Depth-limited search helper function.

        Args:
            node (int): The current node.
            depth (int): The current depth limit.

        Returns:
            bool: True if the goal node is found, False otherwise.
        """
        if node not in visited:
            visited.append(node)
            if node == goal or depth == 0:
                return node == goal
            elif depth > 0:
                for neighbor in sorted(graph[node], reverse=True):
                    if dls_dict(neighbor, depth - 1):
                        return True
        return False

    for depth in range(max_depth + 1):
        visited: List[int] = []
        if dls_dict(start, depth):
            return visited
    return None

def main() -> None:
    """Main function to demonstrate dictionary-based graph search."""
    graph: Dict[int, List[int]] = create_graph_dict()
    start_node: int = 1
    goal_node: int = 11
    max_depth: int = 5

    bfs_visited: List[int] = bfs_dict(graph, start_node, goal_node)
    dfs_visited: List[int] = dfs_dict(graph, start_node, goal_node)
    ids_visited: List[int] = ids_dict(graph, start_node, goal_node, max_depth) or []

    print(f"BFS (Dictionary): {bfs_visited}")
    print(f"DFS (Dictionary): {dfs_visited}")
    print(f"IDS (Dictionary): {ids_visited}")

if __name__ == "__main__":
    main()
