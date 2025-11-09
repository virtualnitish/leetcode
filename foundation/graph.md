# Graph and Graph Traversal Algorithms

# Building and Traversing Graph using Adjacency List

## Adjacency List DFS

### Recursive

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

### Iterative

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



## Adjacency List BFS

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

---

# Shortest Path Algorithm

## Bellman-Ford Algorithm

```python
from collections import defaultdict

def bellman_ford(n, edges, src):
    """
    Computes shortest path from src to all nodes using Bellman-Ford algorithm.
    Returns (distances list, has_negative_cycle flag)
    """
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0

    # Relax edges (n - 1) times
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break  # Early stop if no changes

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return [], True  # Negative cycle detected

    # Format unreachable nodes
    dist = [d if d < INF else -1 for d in dist]
    return dist, False

# Example graph
n = 5
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]
src = 0

distances, has_negative_cycle = bellman_ford(n, edges, src)
if has_negative_cycle:
    print("Graph contains a negative-weight cycle.")
else:
    print("Shortest distances from node", src, ":", distances)

```

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



#### ⛔ What Happens If You Go Beyond `n−1`?

That’s when Bellman-Ford shifts gears — and starts detecting negative weight cycles.

Here's what you do:
- After `n−1` passes, you **do one more pass**.
- If *any* distance improves in that final pass, it means the graph contains a **negative weight cycle** — because a shortest path with more than `n−1` edges implies revisiting nodes and reducing cost repeatedly, which only happens in such a cycle.

So, continuing beyond `n−1` is useful only to check whether **distance is still decreasing due to a loop** — which would violate the well-defined concept of a shortest path.



#### 🧠 In short

- **`n−1` iterations**: explore all shortest paths without cycles.
- **1 extra iteration**: detect negative cycles.
- **More than that**: not useful — just wastes time or risks infinite loops in naïve implementations.

### Impact of Reversing the Relaxation Condition in Bellman–Ford

#### 1. What the Change Does

Changing  
```
if dist[u] != INF and dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
```
to  
```
if dist[u] != INF and dist[v] + w < dist[u]:
    dist[u] = dist[v] + w
```
swaps the roles of the “from” and “to” node in each edge relaxation. Instead of pushing shorter paths outward from already-settled nodes, it attempts to pull updates backward into the source end of each edge. That breaks the forward-propagation logic that Bellman–Ford relies on.



#### 2. Example Walkthrough 

Just skim thorough the example, no need to understand it too much, read the 3rd point for explanation.

#### 2.1 Original Implementation

Graph (n = 5, src = 0):

Edges  
0→1 (−1), 0→2 (4), 1→2 (3), 1→3 (2), 1→4 (2), 3→2 (5), 3→1 (1), 4→3 (−3)

Distances by iteration:

| Iteration | Node 0 | Node 1 | Node 2 | Node 3 | Node 4 |
|-----------|--------|--------|--------|--------|--------|
| 0         | 0      | INF    | INF    | INF    | INF    |
| 1         | 0      | −1     | 2      | −2     | 1      |
| 2         | 0      | −1     | 2      | −2     | 1      |

After one full pass, all shortest paths from 0 settle correctly. A second pass sees no changes, so the algorithm stops early.

#### 2.2 Modified Implementation

Using the reversed condition:

| Iteration | Node 0 | Node 1 | Node 2 | Node 3 | Node 4 |
|-----------|--------|--------|--------|--------|--------|
| 0         | 0      | INF    | INF    | INF    | INF    |
| 1         | 0      | INF    | INF    | INF    | INF    |
| 2         | 0      | INF    | INF    | INF    | INF    |

No edge ever propagates a finite value into its head vertex, so all other distances remain INF. Even if you removed early stopping, nothing ever changes beyond the source.



#### 3. Why This Breaks Bellman–Ford

- Bellman–Ford is built around **forward relaxation**: from a known shortest distance `dist[u]`, you compute `dist[v] = dist[u] + w`.  
- By flipping to `dist[v] + w < dist[u]`, you try to update `u` based on `v`. But `v` starts as INF, so you never “seed” new finite distances.  
- You lose the directional flow of information from the source to other nodes, so no shortest paths ever propagate.



#### 4. Role of the `dist[u] != INF` Check

- It guards against relaxing edges **from** unreachable nodes.  
- If you omit it and use a large numeric sentinel for INF (e.g., 10⁹), `dist[u] + w` might wrap around or become artificially small, letting unreachable nodes erroneously update their neighbors.  
- Semantically, it enforces “only relax edges out of nodes that we already know how to reach.”

Despite its simplicity, the orientation of the relaxation test is critical. Bellman–Ford converges by pushing shortest‐path estimates **forward** along each directed edge. Reversing that direction starves the algorithm of new information and completely breaks convergence.


---


### Dijkstra's Algorithm
[THE CODE IS NOT REVIEWED YET; IT WAS GENERATED BY CHATGPT FOR A QUICK REFERENCE]

```python
import heapq

def dijkstra(n, edges, src):
    """
    Computes shortest path from src to all nodes using Dijkstra's algorithm.
    Returns distances list.
    """
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0

    # Build adjacency list with weights
    adj = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        # If undirected, also add: adj[v].append((u, w))

    heap = [(0, src)]  # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # Already found a better path

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    # Format unreachable nodes
    dist = [d if d < INF else -1 for d in dist]
    return dist

# Example graph
n = 5
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3),
    (3, 4, 1)
]
src = 0

distances = dijkstra(n, edges, src)
print("Shortest distances from node", src, ":", distances)
```

