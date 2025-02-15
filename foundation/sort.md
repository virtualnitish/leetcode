# Sort

## Merge Sort

- **Time Complexity:** `O(n log(n))`
- **Space Complexity:**
  - **Best case:** `O(n)` auxiliary space
  - **Worst case:** `O(n)` auxiliary space


```python
class Solution:
    def merge(self, arr, l, m, r):
        # Create copies of subarrays
        left_arr = arr[l:m+1]
        right_arr = arr[m+1:r+1]
        
        i = 0  # Initial index of left_arr
        j = 0  # Initial index of right_arr
        k = l  # Initial index of merged subarray in arr
        
        # Merge the temp arrays back into arr[l..r]
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_arr, if any
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        # Copy the remaining elements of right_arr, if any
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
                    
    def mergeSort(self, arr, l, r):
        if l < r:
            # Find the middle point
            mid = (r + l) // 2
            
            # Sort first and second halves
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            
            # Merge the sorted halves
            self.merge(arr, l, mid, r)
            
# Example Usage
solution = Solution()
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
solution.mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
```

## Topological Sort

**Depth-First Search (DFS) Postorder Implementation**

```python
from collections import defaultdict

def topological_sort(vertices, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)  # Append after visiting all neighbors

    for vertex in vertices:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]  # Reverse to get the topological order

# Example usage:
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'D'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'E'),
    ('E', 'F')
]

order = topological_sort(vertices, edges)
print("Topological Order:", order)
```

**Sample Output:**
```
Topological Order: ['C', 'B', 'A', 'D', 'E', 'F']
```

---

1. **Explanation of the Approach:**

   The algorithm uses **Depth-First Search (DFS)** to traverse the graph. Here's the key idea:

   - **Recursive DFS Traversal:** For each unvisited node, we recursively visit all its unvisited neighbors.
   - **Post-order Insertion:** After all neighbors of a node have been visited, the node is appended to a stack. This ensures that a node appears after all nodes it depends on.
   - **Reverse the Stack:** Reversing the stack gives the nodes in a topologically sorted order.

2. **Time & Space Complexity:**

   - **Time Complexity:** O(V + E)
     - *V* is the number of vertices, and *E* is the number of edges.
     - Each vertex and edge is explored once during DFS.
   - **Space Complexity:** O(V + E)
     - O(V + E) for storing the graph in an adjacency list.
     - O(V) for the recursion call stack in the worst case (if the graph is a single linear chain).
     - O(V) for the `visited` set and `stack` to store the topological order.

---

**Additional Insight:**

Topological sorting is fundamental in scenarios where there is a need to schedule tasks while respecting dependencies, such as compiling programs, task scheduling, and resolving symbol dependencies in linkers. If you're interested in handling graphs with cycles (which cannot be topologically sorted), you might consider incorporating cycle detection into your algorithm.

