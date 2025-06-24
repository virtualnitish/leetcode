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
    if node not in visited: # Not required if DFS is only called after checking the visited set
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
        if node not in visited: # Essential check
            visited.add(node)
            result.append(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return result
```

**The Line `if node not in visited:` Before Marking Visited Is Very Very Important.**   

Even though we only add neighbors that haven't been visited to the stack, **a node can be added to the stack before it has been processed (i.e., marked as visited)** from multiple sources.

```
    1
   / \
  2---3
       \
        4
```

In graphs with cycles or multiple paths, a node might get added to the stack by different neighboring nodes before it's actually popped and processed.

**Illustration:**

- Node `2` was connected to both `1` and `3`.
- Both `1` and `3` can add `2` to the stack before `2` is processed.
- Without the `if node not in visited:` check, `2` is processed multiple times and added to the result twice!
- **Final Result:** `[1, 3, 4, 2, 2]`



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

### Bellman-Ford Algorithm

```python
from typing import List

class Solution:
    def bellmanFord(self, n: int, edges: List[List[int]], src: int) -> List[int]:
        """
        Compute shortest paths from src to all nodes in a weighted directed graph
        using the Bellman–Ford algorithm.  
        
        :param n: Number of nodes, labeled 0 to n-1
        :param edges: List of edges [u, v, w] where u→v has weight w
        :param src: Starting node
        :return: 
          - If no negative cycle is reachable from src, returns a list dist[] of length n,
            where dist[i] is the shortest distance from src to i (or -1 if i is unreachable).
          - If a negative-weight cycle is reachable, returns an empty list [].
        """
        # ————— Edge-case handling —————
        if n <= 0 or not (0 <= src < n):
            return []
        
        # Initialize distances
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        
        # Relax all edges up to (n-1) times
        for _ in range(n - 1):
            updated = False
            # We snapshot the distances so each pass only uses previous values
            next_dist = dist.copy()
            
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < next_dist[v]:
                    next_dist[v] = dist[u] + w
                    updated = True
            
            dist = next_dist
            # Early exit if no update in this pass
            if not updated:
                break
        
        # Check for negative-weight cycles reachable from src
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                # Negative cycle detected
                return []
        
        # Convert unreachable distances from INF to -1
        return [d if d < INF else -1 for d in dist]
```


Great question, Nitish — this goes right to the heart of why Bellman-Ford works so elegantly for general graphs, even with negative weights.

---

#### 🚧 Why **n−1** Iterations?

In a graph with **n** nodes, the **longest possible simple path** (a path that doesn’t repeat any nodes) contains at most **n−1 edges**.

That’s because any path with **n** or more edges must have visited at least one node twice — and hence contains a cycle.

So, the **shortest path to any node** — without cycles — can be found in at most **n−1 edge relaxations** from the source. Each iteration potentially adds one more edge to the shortest path you're building.

Thus:
- **1st pass**: explores paths with 1 edge
- **2nd pass**: paths with ≤ 2 edges
- ...
- **(n−1)th pass**: allows up to (n−1) edges (longest simple path)

By the end of pass `n−1`, you've explored all possible shortest paths that don’t involve cycles — and you’re done.

---

#### ⛔ What Happens If You Go Beyond `n−1`?

That’s when Bellman-Ford shifts gears — and starts detecting negative weight cycles.

Here's what you do:
- After `n−1` passes, you **do one more pass**.
- If *any* distance improves in that final pass, it means the graph contains a **negative weight cycle** — because a shortest path with more than `n−1` edges implies revisiting nodes and reducing cost repeatedly, which only happens in such a cycle.

So, continuing beyond `n−1` is useful only to check whether **distance is still decreasing due to a loop** — which would violate the well-defined concept of a shortest path.

---

#### 🧠 In short

- **`n−1` iterations**: explore all shortest paths without cycles.
- **1 extra iteration**: detect negative cycles.
- **More than that**: not useful — just wastes time or risks infinite loops in naïve implementations.

Let me know if you want a tiny graph to visualize this live. It’s pretty fun watching a negative cycle unravel distance values like a slot machine. 🎰