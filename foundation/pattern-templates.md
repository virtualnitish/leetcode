# Popular Patterns Templates

---

### 1. **Sliding Window**
**Use Case**: Subarrays/substrings with specific constraints (e.g., longest substring without repeating characters).
```python
def sliding_window(s: str) -> int:
    window = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        # Add s[right] to window
        window[s[right]] = window.get(s[right], 0) + 1
        
        # Check if window is invalid
        while window[s[right]] > 1:  # Example condition
            # Remove s[left] from window
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        
        # Update result
        max_len = max(max_len, right - left + 1)
    return max_len
```
**Example**: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

### 2. **Two Pointers**
**Use Case**: Sorted arrays, pairwise comparisons (e.g., two-sum, merging sorted arrays).
```python
def two_pointers(arr: list) -> list:
    left = 0
    right = len(arr) - 1
    while left < right:
        # Process logic here (e.g., check sum)
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return []
```
**Example**: [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

---

### 3. **Fast & Slow Pointers (Floyd's Cycle)**
**Use Case**: Linked list cycle detection, find middle of a linked list.
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
**Example**: [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

---

### 4. **BFS (Level Order)**
**Use Case**: Shortest path, level-order traversal.
```python
from collections import deque

def bfs(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result
```
**Example**: [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

---

### 5. **DFS (Recursive)**
**Use Case**: Tree/graph traversal, backtracking.
```python
def dfs(node, path, result):
    if not node:
        return
    # Process current node
    path.append(node.val)
    if not node.left and not node.right:  # Leaf node check
        result.append(list(path))
    dfs(node.left, path, result)
    dfs(node.right, path, result)
    path.pop()  # Backtrack
```
**Example**: [Path Sum II](https://leetcode.com/problems/path-sum-ii/)

---

### 6. **Backtracking**
**Use Case**: Permutations, subsets, combinations.
```python
def backtrack(nums, path, result):
    if len(path) == len(nums):
        result.append(list(path))
        return
    for num in nums:
        if num in path:
            continue
        path.append(num)
        backtrack(nums, path, result)
        path.pop()

def permute(nums):
    result = []
    backtrack(nums, [], result)
    return result
```
**Example**: [Permutations](https://leetcode.com/problems/permutations/)

---

### 7. **Binary Search**
**Use Case**: Sorted arrays, rotated arrays, search boundaries.
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
**Example**: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

### 8. **Merge Sort (Merge K Sorted Lists)**
**Use Case**: Merge intervals, external sorting.
```python
import heapq

def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i))
    dummy = ListNode()
    curr = dummy
    while heap:
        val, idx = heapq.heappop(heap)
        curr.next = ListNode(val)
        curr = curr.next
        if lists[idx].next:
            lists[idx] = lists[idx].next
            heapq.heappush(heap, (lists[idx].val, idx))
    return dummy.next
```
**Example**: [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

---

### 9. **Dynamic Programming (Tabulation)**
**Use Case**: Optimization problems (e.g., Fibonacci, knapsack).
```python
def dp_template(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case
    for i in range(1, n + 1):
        # Update dp[i] based on previous states
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```
**Example**: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

---

### 10. **Cyclic Sort**
**Use Case**: Arrays with elements in a range (e.g., [1..n]).
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    return nums
```
**Example**: [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

---

### 11. **Topological Sort (Kahn's Algorithm)**
**Use Case**: Scheduling tasks with dependencies.
```python
from collections import deque

def topological_sort(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses
    for course, pre in prerequisites:
        adj[pre].append(course)
        in_degree[course] += 1
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == numCourses else []
```
**Example**: [Course Schedule](https://leetcode.com/problems/course-schedule/)

---

### 12. **Trie**
**Use Case**: Word validation, prefix search.
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
```
**Example**: [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)

---

### 13. **Monotonic Stack**
**Use Case**: Next greater element, stock span.
```python
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```
**Example**: [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

---

### 14. **Heap/Priority Queue**
**Use Case**: Kth largest/smallest, merge intervals.
```python
import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```
**Example**: [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

---

### 15. **Intervals (Merge/Insert)**
**Use Case**: Overlapping intervals, scheduling.
```python
def merge(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
```
**Example**: [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

---

### 16. **Bit Manipulation**
**Use Case**: Counting set bits, XOR tricks.
```python
def count_bits(n):
    count = 0
    while n:
        n &= n - 1  # Clear the least significant set bit
        count += 1
    return count
```
**Example**: [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

---

### 17. **Union-Find (Disjoint Set)**
**Use Case**: Connected components, cycle detection.
```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
```
**Example**: [Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

---

### 18. **Memoization (Dynamic Programming)**
**Use Case**: Overlapping subproblems (e.g., Fibonacci).
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
**Example**: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

---

These templates cover most common patterns. Adapt them to specific problems by adjusting variables, conditions, and return values. Practice recognizing which pattern fits a problem's constraints!