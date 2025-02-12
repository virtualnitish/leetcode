# Graph and Graph Traversal Algorithms

## Building and Traversing Graph usnig Adjacency List

### Adjacency List DFS

```python
def build_adj_list(edges, n): # n is number of vertices
    adj_list = {i: [] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Assuming it's an undirected graph
    return adj_list

def dfs(adj_list, start, visited):
    visited.add(start)
    print(start, end=' ')
    for neighbor in adj_list[start]:
        if neighbor not in visited:
            dfs(adj_list, neighbor, visited)

# Example usage:
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
n = 7  # Number of nodes

# Build the adjacency list
graph = build_adj_list(edges, n)
print("Adjacency List:", graph)

# Perform DFS starting from node 0
visited = set()
print("DFS traversal:", end=' ')
dfs(graph, 0, visited)
```

### Adjacency List BFS

```python
from collections import deque

def build_adj_list(edges, n):
    adj_list = {i: [] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Assuming it's an undirected graph
    return adj_list

def bfs(adj_list, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    bfs_order = []

    while queue:
        u = queue.popleft()
        bfs_order.append(u)
        for neighbor in adj_list[u]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return bfs_order

# Example usage:
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
n = 7  # Number of nodes

# Build the adjacency list
graph = build_adj_list(edges, n)
print("Adjacency List:", graph)

# Perform BFS starting from node 0
bfs_result = bfs(graph, 0)
print("BFS traversal:", bfs_result)
```

## Shortest Path 

