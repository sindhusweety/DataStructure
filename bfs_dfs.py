from collections import deque

# Graph definition (Adjacency List)
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1, 5], 5: [2, 4]}


# Algorithms
def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def dfs_recursive(graph: dict[int, list[int]], start: int) -> list[int]:
    visited = set()
    result = []

    def traverse(node: int) -> None:
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                traverse(neighbor)

    if start in graph:
        traverse(start)
    return result


def dfs_iterative(graph: dict[int, list[int]], start: int) -> list[int]:
    if start not in graph:
        return []

    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return result


# Run test cases
if __name__ == "__main__":
    start_node = 0

    print("Input Graph:", graph)
    print("Start Node :", start_node)
    print("-" * 40)
    print("BFS Traversal           :", bfs(graph, start_node))
    print("DFS Recursive Traversal :", dfs_recursive(graph, start_node))
    print("DFS Iterative Traversal :", dfs_iterative(graph, start_node))
