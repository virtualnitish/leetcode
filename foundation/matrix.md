# Matrix

## DFS

*Recursive Algorithm; Backtracking is involved.*

DFS code to count all distinct paths from start to destination.

```python
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (
        min(r,c) < 0 or r >= ROWS or c >= COLS or
        (r, c) in visit or grid[r][c] == 1
    ):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    # Direction vectors for moving up, down, left, and right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = 0
    for dr, dc in directions:
        count += dfs(grid, r + dr, c + dc, visit)

    visit.remove((r, c))
    return count

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
print(dfs(grid, r, c, set()))
```

### DFS Steps to remember

1. Start with Terminating conditions
    1. Failure
    2. Success
2. Add to visited
3. Recurve all neighbors
4. Remove from visited
5. Return count


## BFS

BFS code to find the shortest path length from start to destination.

```python
from collections import deque

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque([(0, 0)])
    visit.add((0, 0))
    length = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    (nr, nc) not in visit and grid[nr][nc] == 0
                    ):
                    queue.append((nr, nc))
                    visit.add((nr, nc))
        length += 1
    
    return -1  # If there's no valid path

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
print(bfs(grid))  # Output: shortest path length

```

**Time Complexity:** `O(rows*cols)`    
**Space Complexity:** `O(rows*cols)`

### Steps to remember:

1. Define variables like length, visited and queue.
2. Two loops; while and for; restrict for with length of queue.
3. Check terminating condition
4. Three checks to add the neighbour:
    1. Out-of-bounds check
    2. Visited check
    3. Obstacle check
5. Increase length for level
6. Return length

---

## 🌐 Understanding DFS in Matrices

### **1. Grasping the Matrix as a Graph**

A matrix can be visualized as a grid of nodes, where each cell represents a node, and edges connect adjacent cells.

- **Adjacency**: Typically, each cell is adjacent to its neighboring cells (up, down, left, right). Some problems also consider diagonal neighbors.
- **Graph Representation**: The matrix itself acts as an implicit graph; you don't need to build an explicit adjacency list or matrix.

### **2. Core Components of DFS in a Matrix**

Implementing DFS in a matrix involves a few essential elements:

1. **Traversal Function**: A recursive `dfs(r, c)` function that explores neighboring cells.
2. **Boundary Checks**: Ensuring the next cell is within the matrix bounds.
3. **Visited Tracking**: Keeping track of visited cells to prevent infinite loops.
4. **Problem-Specific Conditions**: Conditions that dictate whether to continue traversal from a cell.

---

## 🛠️ Implementing DFS: Step by Step

Let's dissect the DFS implementation with a generic template.

### **Step 1: Initialize**

```python
def dfs(r, c):
    # Base case checks will go here
    # Mark the cell as visited
    # Explore neighboring cells
```

### **Step 2: Base Case and Boundary Checks**

Before proceeding with recursion, check for:

- **Bounds**: `0 <= r < rows` and `0 <= c < cols`
- **Visited Cells**: Avoid re-visiting cells
- **Obstacle Conditions**: Depending on the problem (e.g., walls, water)

```python
def dfs(r, c):
    if (r < 0 or c < 0 or r >= rows or c >= cols):
        return
    if (r, c) in visited:
        return
    if matrix[r][c] == obstacle_value:
        return
```

### **Step 3: Mark the Cell and Explore Neighbors**

```python
    visited.add((r, c))
    for dr, dc in directions:
        dfs(r + dr, c + dc)
```

**Directions**: Define the possible movements.

```python
directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
```

---


## When to Mark a node as visited?!

Absolutely, I get where you're coming from. Figuring out **when** to mark a node as visited in DFS or BFS can be a bit tricky, but once you grasp the underlying principles, it becomes much clearer. Let's dive deep and unravel this together.

---

## 🧭 The Crux of Marking Nodes as Visited

At the heart of DFS and BFS lies the need to **prevent cycles** and **avoid redundant processing** of nodes. Marking a node as visited ensures that:

- **We don't revisit the same node** multiple times.
- **We prevent infinite loops** in cyclic graphs.

The timing of when we mark a node as visited can affect the correctness and efficiency of your traversal.


### **When to Mark a Node as Visited in DFS**

**Best Practice**: **Mark a node as visited **when you first encounter it**, before exploring its neighbors.**


### **When to Mark a Node as Visited in BFS**

**Best Practice**: **Mark a node as visited **when you enqueue it**, before it's dequeued for processing.**


---

## 🌳 Depth-First Search (DFS)

### **When to Mark a Node as Visited in DFS**

**Best Practice**: **Mark a node as visited **when you first encounter it**, before exploring its neighbors.**

### **Why?**

- **Avoid Reprocessing**: By marking the node early, you ensure that if you encounter it again (possibly through a different path), you won't process it again.
- **Prevent Infinite Recursion**: In recursive implementations, marking early prevents the function from calling itself infinitely in the presence of cycles.

### **DFS Implementation Details**

Let's consider recursive DFS on a graph represented using an adjacency list.

**Recursive DFS Function:**

```python
def dfs(node):
    # Mark the node as visited
    visited.add(node)
    # Process the node if needed
    # Explore neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
```

**Key Point**: The node is marked as visited **immediately upon entering the function**, before any neighbor exploration.

### **Understanding with an Example**

Imagine a simple graph:

```
A -- B
|    |
C -- D
```

Starting DFS from `A`:

1. **Visit `A`**: Mark as visited.
2. **Neighbors of `A`**: `B` and `C`.
3. **Visit `B`**:
   - Mark `B` as visited.
   - Neighbor `D`.
   - Visit `D`:
     - Mark `D` as visited.
     - Neighbor `C`.
     - `C` is unvisited; proceed.
4. **Visit `C`**:
   - Mark `C` as visited.
   - Neighbor `A` (already visited), so skip.
   
By marking nodes upon entering `dfs`, we avoid revisiting nodes and prevent infinite loops.

---

## 🚣 Breadth-First Search (BFS)

### **When to Mark a Node as Visited in BFS**

**Best Practice**: **Mark a node as visited **when you enqueue it**, before it's dequeued for processing.**

### **Why?**

- **Avoid Multiple Enqueueing**: By marking nodes as visited when enqueuing, you prevent the same node from being added to the queue multiple times.
- **Ensure Correct Level Order**: In BFS, we traverse level by level. Marking upon enqueue ensures that each node is processed at the correct level.

### **BFS Implementation Details**

Here's a typical BFS implementation using a queue:

```python
from collections import deque

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited.add(start_node)
    while queue:
        node = queue.popleft()
        # Process the node if needed
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
```

**Key Point**: Nodes are marked as visited **when they are added to the queue**, not when they are dequeued.

### **Understanding with an Example**

Using the same graph as before, starting BFS from `A`:

1. **Enqueue `A`**: Mark `A` as visited.
2. **Dequeue `A`**:
   - Neighbors: `B` and `C`.
   - Enqueue `B` and `C`; mark both as visited.
3. **Dequeue `B`**:
   - Neighbor `D`.
   - Enqueue `D`; mark as visited.
4. **Dequeue `C`**:
   - Neighbors `A` (already visited) and `D` (already visited); skip.
5. **Dequeue `D`**:
   - Neighbors `B` and `C` (both visited); skip.

---

## 🧐 Why the Difference in Timing?

### **DFS vs. BFS**

- **DFS** explores as far as possible along each branch before backtracking. Marking nodes upon entering the `dfs` function ensures that we don't revisit nodes during this deep exploration.
- **BFS** explores neighbor nodes level by level. Marking nodes when enqueuing prevents multiple enqueues of the same node, maintaining the correct order.

---

## 🌀 Common Confusions and Clarifications

### **1. Marking During Neighbor Exploration**

Sometimes, you might see code where nodes are marked as visited during the neighbor exploration loop. For example:

```python
def dfs(node):
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor)
```

**Why This Can Be Problematic**:

- **Risk of Missing Processing on Current Node**: If you process the node (e.g., accumulate values, check conditions) before marking it as visited, you might process it multiple times.
- **Less Clear Logic**: Marking nodes in multiple places can make the code harder to read and debug.

**Best Practice**: Stick to marking nodes as visited at a consistent point—preferably at the start of the function (DFS) or when adding to the queue (BFS).

### **2. Using Visited Sets vs. Inherent Data Structure**

In some problems, the graph might be represented in such a way that you can modify the node or edge data to indicate visitation (like changing a value in a matrix). Be cautious:

- **Modifying Input Data**: Only do this if the problem allows mutation.
- **Using Visited Structures**: If you can't modify the input, use an auxiliary data structure like a `visited` set or array.

---

## 📐 Matrix-Specific Considerations

When working with matrices, especially in grid traversal problems, similar principles apply.

### **DFS in Matrices**

```python
def dfs(r, c):
    # Mark as visited
    visited.add((r, c))
    # Explore neighbors
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc) and (nr, nc) not in visited:
            dfs(nr, nc)
```

### **BFS in Matrices**

```python
def bfs(start_r, start_c):
    queue = deque()
    queue.append((start_r, start_c))
    visited.add((start_r, start_c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.add((nr, nc))
```

---

## 📝 Tips to Remember

### **1. Mark Early to Prevent Redundancy**

- **DFS**: Mark at the beginning of the function.
- **BFS**: Mark when enqueuing the node.

### **2. Consistency is Key**

- Choose a consistent point in your code to mark nodes.
- This reduces confusion and potential bugs.

### **3. Think About the Traversal Order**

- **DFS**: Deep exploration; marking early prevents revisiting during recursion.
- **BFS**: Level-wise exploration; marking upon enqueue ensures correct order.

### **4. Avoid Marking Nodes Multiple Times**

- Once a node is marked as visited, you shouldn't mark it again.
- This prevents unnecessary processing and infinite loops.

---

## 🌟 Putting It All Together with an Example

Let's consider a maze represented as a grid:

- `0` represents an open path.
- `1` represents a wall.

**Goal**: Find a path from the start to the end.

### **DFS Implementation**

```python
def dfs(r, c):
    if not is_valid(r, c) or grid[r][c] == 1 or (r, c) in visited:
        return False
    if is_end(r, c):
        return True
    visited.add((r, c))
    for dr, dc in directions:
        if dfs(r + dr, c + dc):
            return True
    return False
```

- **Visited Marking**: Done immediately after passing base cases.
- **Why**: Ensures we don't revisit the same cell, avoiding infinite recursion.

---

## 🔄 Final Thoughts

Understanding **when** to mark a node as visited boils down to:

- **DFS**: Mark upon entering the node's processing to prevent re-exploration in the recursion stack.
- **BFS**: Mark when a node is discovered and added to the queue to maintain traversal order.

Always consider:

- **Traversal Strategy**: How does your algorithm flow through the graph?
- **Prevention of Reprocessing**: How can you avoid unnecessary work?
- **Cycle Detection**: How do you prevent infinite loops in cyclic graphs?

---

By internalizing these principles and consistently applying them, you'll gain confidence in implementing DFS and BFS across various problems. Practice with different scenarios—graphs, trees, matrices—and soon this confusion will transform into clarity.

Feel free to throw another question my way or if there's a particular example you'd like to dissect further. I'm here to help you master these concepts!