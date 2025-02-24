# Disjoint Set

## Without Rank(or Size)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path Compression
        return self.parent[u]
        
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u  # Union without considering rank
```


## With Rank

```python
class DisjointSet:
    def __init__(self, n):
        # Each element is parent of itself to form an individual disjoint set.
        self.parent = list(range(n)) # [0,1,2,3,...]
        self.rank = [0] * n

    def find(self, u):
        # If a set is not parent of itself, then use path compression
        # to find the root(topmost parent) of the disjoint set.
        ## Gets into work when you have started to form new disjoint sets and 
        ## other individual sets have joined you already.
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by rank to attach smaller tree under the larger tree
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Example usage:
# Create a Disjoint Set with 5 elements (0 to 4)
ds = DisjointSet(5)

# Union operations
ds.union(0, 1)
ds.union(1, 2)
ds.union(3, 4)

# Find operations
print(ds.find(0))  # Outputs: 0 (or the representative of the set containing 0)
print(ds.find(1))  # Outputs: 0 (or the representative of the set containing 1)
print(ds.find(3))  # Outputs: 3 (or the representative of the set containing 3)

# Check if two elements are in the same set
print(ds.find(0) == ds.find(1))  # Outputs: True
print(ds.find(0) == ds.find(3))  # Outputs: False
```

# Deep Dive

Let's dive deep into the heart of Union-Find and Disjoint Set data structures. You've spotted an implementation of Union-Find that doesn't use `rank`, and it's piqued your curiosity. Can Union-Find work without `rank`? Absolutely. But let's explore how that affects the structure and performance, and understand these concepts in depth.

### **Understanding Disjoint Set (Union-Find) Data Structure**

At its core, the Disjoint Set (also known as Union-Find) data structure keeps track of elements partitioned into a number of disjoint (non-overlapping) sets. It supports two primary operations:

1. **Find**: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
2. **Union**: Merge two subsets into a single subset.

These operations are crucial in many algorithms, like Kruskal's algorithm for finding Minimum Spanning Trees, where you need to efficiently track connected components.

### **The Role of `rank` in Union-Find**

- **Purpose of `rank`**: The `rank` (or sometimes `size`) heuristic is an optimization technique used to keep the tree representing each set as flat as possible. The `rank` typically represents the approximate height of the tree.
- **Union by Rank**: When performing a union, you attach the tree with a lower `rank` under the root of the tree with a higher `rank`. This helps prevent the trees from becoming tall, which keeps operations efficient.

### **Union-Find Without `rank`**

Yes, Union-Find can work without the `rank`. The version you provided:

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x  # Union without considering rank
```

- **Functionality**: It correctly merges sets and tracks connected components.
- **Performance**: Without `rank`, the trees can become unbalanced, potentially growing tall in pathological cases. However, this risk is mitigated significantly by **path compression** in the `find` method.

### **Path Compression**

- **What It Does**: Path compression flattens the structure of the tree whenever you perform a `find` operation by making each node along the path point directly to the root.
- **Impact on Performance**: This optimization alone is powerful and often sufficient to keep the operations nearly constant time on average.

### **Performance Analysis**

- **Without `rank`, with Path Compression**:
  - **Time Complexity**: Amortized O(α(N)), where α(N) is the inverse Ackermann function, which grows extremely slowly, effectively making it near-constant time.
  - **Practical Performance**: For most practical purposes and input sizes, the absence of `rank` doesn't significantly impact performance due to the efficiency of path compression.

- **Without `rank` and without Path Compression**:
  - **Time Complexity**: Can degrade to O(N) per operation in the worst case, as trees can become tall.

### **Why Use `rank`?**

- **Preventing Tall Trees**: The `rank` heuristic ensures that the tree heights remain logarithmic, which, combined with path compression, guarantees nearly constant time per operation.
- **Worst-Case Scenarios**: While path compression is effective, combining it with `rank` guards against specific patterns of unions that could otherwise degrade performance.

### **Deep Dive into the Code**

Let's break down the implementation you've seen:

#### **Initialization**

```python
def __init__(self, size):
    self.parent = list(range(size))
```

- **Setting up Parents**: Each element is initially its own parent, meaning every element starts as a separate set.

#### **Find Operation with Path Compression**

```python
def find(self, x):
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])  # Recursively find root and compress path
    return self.parent[x]
```

- **Path Compression**: By updating `self.parent[x]`, every node points directly to the root after a `find`, flattening the structure.

#### **Union Operation without `rank`**

```python
def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x != root_y:
        self.parent[root_y] = root_x  # Attach root of y's tree to root of x's tree
```

- **No `rank` Consideration**: The code always attaches `root_y` under `root_x`, regardless of tree sizes.

### **Metaphor to Clarify**

Imagine each set as a group of friends connected through a leader (the root). Without considering the leader's popularity (`rank`), you always have one group's leader become a follower of another group's leader. If you always make one leader the follower without considering group size, some leaders end up managing a huge group alone, potentially slowing down communication. Using `rank` ensures the leader with the larger group remains in charge, keeping the hierarchy balanced.

### **Potential Drawbacks of Omitting `rank`**

- **Unbalanced Trees**: Over time, especially with certain union patterns, trees might become unbalanced.
- **Increased Heights**: Taller trees mean that without path compression, the `find` operation could become less efficient.

### **Why It Often Doesn't Matter**

- **Effectiveness of Path Compression**: Path compression drastically reduces the actual heights of the trees during `find` operations, mitigating the lack of `rank`.
- **Real-World Data**: Many practical applications don't experience the worst-case union patterns that would cause significant performance degradation.

### **Combining `rank` and Path Compression**

- **Optimal Performance**: Using both optimizations together ensures that even in the worst case, operations remain efficient.
- **Implementation with `rank`**:

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size  # Initialize ranks
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # Union by Rank
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
```

- **Explanation**:
  - **Comparing Ranks**: The tree with the lower rank becomes a subtree of the tree with the higher rank.
  - **Updating Ranks**: If both trees have the same rank, one becomes the root, and its rank increases by one.

### **Should You Use `rank`?**

- **Use Cases Without `rank`**:
  - For simple applications where performance isn't critical.
  - When prioritizing code simplicity and readability.
  - In educational contexts to illustrate the basic mechanics.

- **Use Cases With `rank`**:
  - When dealing with large datasets.
  - In performance-critical applications where you need guaranteed efficiency.
  - When the union patterns could potentially degenerate (e.g., adversarial inputs).

### **Experiment and See**

- **Practical Learning**: Implement both versions and test them with various inputs.
- **Performance Testing**:
  - Create scenarios with different union patterns.
  - Measure the time taken for a large number of operations.

### **Additional Insights**

#### **Union by Size**

- **Alternative to `rank`**: Instead of using tree height (`rank`), you can use the size (number of elements) of each set.
- **Implementation**:

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size  # Initialize sizes
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # Union by Size
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
```

- **Benefit**: This ensures that smaller trees are added under larger ones, keeping trees balanced.

#### **Path Splitting and Path Halving**

- **Further Optimizations**: Variations of path compression that adjust how parents are updated during the `find` operation.
- **Goal**: To optimize the performance of `find` even further.

### **Applications of Union-Find**

- **Graph Algorithms**:
  - **Cycle Detection**: Determining if adding an edge creates a cycle.
  - **Connected Components**: Identifying disconnected subgraphs.

- **Image Processing**:
  - **Image Segmentation**: Grouping pixels into regions.

- **Network Connectivity**:
  - **Dynamic Connectivity Problems**: Maintaining information about connected components as the network changes.

- **Biology and Clustering**:
  - **Species Classification**: Grouping organisms based on genetic similarity.

### **Conclusion**

- **Union-Find Without `rank` Works**: It's functional and, with path compression, often efficient enough for many applications.
- **Performance Considerations**: Including `rank` provides a safety net against potential performance issues.
- **Understanding Trade-offs**: Simplicity vs. optimal efficiency.