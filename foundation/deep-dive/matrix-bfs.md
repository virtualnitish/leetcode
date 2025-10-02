# Matrix BFS Deep Dive

## Why we return `length` (not `length+1`)

Core idea:
- In BFS, `length` equals the number of steps (edges) taken from the start to reach the current level.
- We begin with `length = 0` at the start node (0 steps).
- After processing each level (all nodes at that distance), we increment `length` by 1.
- When we pop the destination, `length` already equals the shortest number of steps to reach it.

Example (grid with S=start, E=end, #=wall):

```
S . . .
# # . .
. . . #
. # . E
```

- Level 0: S (length = 0)
- Level 1: neighbors of S (length = 1) → nodes 1 step away
- Level 2: neighbors of Level 1 (length = 2) → nodes 2 steps away
- …
- When E is reached at level k, shortest path length is exactly k.

Edges vs nodes:
- Paths are measured in edges (moves), not nodes visited.
- If a path is S → A → B → E, edges = 3, nodes = 4.
- BFS `length` is the edge count; returning `length+1` would overcount moves.

Visualization (ripples):
- Ripple 0: nodes 0 steps away (start)
- Ripple 1: nodes 1 step away
- Ripple 2: nodes 2 steps away
- …
- Destination in ripple k → shortest path length = k.

Memory trick:
- If the problem asks for steps/moves → return `length`.
- If the problem asks for number of nodes in the path → return `length + 1`.

Quick rule of thumb:
- Steps = length
- Nodes = length + 1
