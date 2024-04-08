from collections import deque
from typing import Dict, List, Tuple

# Define the graph as a dictionary of integer nodes pointing to lists of integer nodes
graph: Dict[int, List[int]] = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, 9],
    5: [10, 11],  # Goal
    6: [12, 13],
    7: [14, 15],

    # leaf nodes
    8: [],
    9: [],
    10: [],
    11: [],  # Goal
    12: [],
    13: [],
    14: [],
    15: []
}

def bfs(graph: Dict[int, List[int]], start: int, goal: int) -> List[int]:
    visited: List[int] = []
    queue: deque = deque([start])

    while queue:
        node: int = queue.popleft()
        if node == goal:
            visited.append(node)
            return visited
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])

    return visited

def dfs(graph: Dict[int, List[int]], start: int, goal: int) -> List[int]:
    visited: List[int] = []
    stack: List[int] = [start]

    while stack:
        node: int = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            stack.extend(reversed(graph[node]))

    return visited

def iddfs(graph: Dict[int, List[int]], start: int, goal: int) -> Tuple[List[int], List[int]]:
    visited_order: List[int] = []
    path_to_goal: List[int] = []

    def dls(node: int, depth: int, path: List[int]) -> bool:
        if node not in path:
            visited_order.append(node)

        if node == goal:
            path_to_goal.extend(path + [node])
            return True
        
        if depth == 0:
            return False
        
        for neighbour in graph[node]:
            if dls(neighbour, depth - 1, path + [node]):
                return True
            
        return False

    depth = 0
    while not dls(start, depth, []):
        depth += 1
        if depth > len(graph):
            break

    return visited_order, path_to_goal

# Run each search algorithm
bfs_order: List[int] = bfs(graph, 1, 11)
dfs_order: List[int] = dfs(graph, 1, 11)
iddfs_order: Tuple[List[int], List[int]] = iddfs(graph, 1, 11)

bfs_order, dfs_order, iddfs_order



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
