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
