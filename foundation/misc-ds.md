# Misc. Data Structures

## Disjoint Set

### Without Rank(or Size)

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

### With Rank

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

[Disjoint-Set Deep Dive](deep-dive/disjoint-set.md)