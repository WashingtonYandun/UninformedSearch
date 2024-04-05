from typing import List

class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.adjacent_nodes: List[Node] = []

def breadth_first_search(start_node: Node, goal: int) -> List[int]:
    visited: List[int] = []
    queue: List[Node] = [start_node]
    
    while queue:
        node: Node = queue.pop(0)
        if node.value == goal:
            return visited
        
        visited.append(node.value)
        for child in node.adjacent_nodes:
            if child.value not in visited and child not in queue:
                queue.append(child)
    return visited

def depth_first_search(start_node: Node, goal: int, visited: List[int] = None) -> List[int]:
    if visited is None:
        visited = []
    
    visited.append(start_node.value)
    if start_node.value == goal:
        return visited
    
    for child in start_node.adjacent_nodes:
        if child.value not in visited:
            result: List[int] = depth_first_search(child, goal, visited)
            if result:
                return visited
    return visited

def iterative_deepening_dfs(start_node: Node, goal: int) -> List[int]:
    def dfs(node: Node, goal: int, depth: int, visited: List[int]) -> bool:
        if node.value == goal:
            return True
        if depth <= 0:
            return False
        
        visited.append(node.value)
        for child in node.adjacent_nodes:
            if child.value not in visited:
                if dfs(child, goal, depth-1, visited):
                    return True
        visited.pop()
        return False
    
    depth: int = 0
    visited: List[int] = []
    while True:
        if dfs(start_node, goal, depth, visited):
            return visited
        depth += 1
        visited = []

# Define the graph using Node objects
node1: Node = Node(1)
node2: Node = Node(2)
node3: Node = Node(3)
node4: Node = Node(4)
node5: Node = Node(5)
node6: Node = Node(6)
node7: Node = Node(7)
node8: Node = Node(8)
node9: Node = Node(9)
node10: Node = Node(10)
node11: Node = Node(11)
node12: Node = Node(12)
node13: Node = Node(13)
node14: Node = Node(14)
node15: Node = Node(15)

node1.adjacent_nodes.extend([node2, node3])
node2.adjacent_nodes.extend([node4, node5])
node3.adjacent_nodes.extend([node6, node7])
node4.adjacent_nodes.extend([node8, node9])
node5.adjacent_nodes.extend([node10, node11])  # Goal node
node6.adjacent_nodes.extend([node12, node13])
node7.adjacent_nodes.extend([node14, node15])

# Perform the searches
bfs_visited: List[int] = breadth_first_search(node1, 11)
dfs_visited: List[int] = depth_first_search(node1, 11)
iddfs_visited: List[int] = iterative_deepening_dfs(node1, 11)

print(bfs_visited)
print(dfs_visited)
print(iddfs_visited)
