# Graph and Graph Traversal Algorithms

## Building and Traversing Graph using Adjacency List

### Adjacency List DFS

#### Recursive

```python
def build_adj_list(edges, n):  # n is the number of vertices
    adj_list = {i: [] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Assuming it's an undirected graph
    return adj_list

def dfs(adj_list, node, visited, result):
    visited.add(node)
    result.append(node)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(adj_list, neighbor, visited, result)

edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
n = 7  # Number of nodes

graph = build_adj_list(edges, n)
print("Adjacency List:", graph)

# Perform DFS starting from node 0
visited = set()
result = []
dfs(graph, 0, visited, result)
print("DFS traversal:", result)
```

#### Iterative

```python
def dfs_iterative(adj_list, start):
    visited = set()
    result = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return result
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

edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
n = 7  # Number of nodes

graph = build_adj_list(edges, n)
print("Adjacency List:", graph)

# Perform BFS starting from node 0
bfs_result = bfs(graph, 0)
print("BFS traversal:", bfs_result)
```

## Shortest Path Algorithm

