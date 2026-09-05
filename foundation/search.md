# Search

## Binary Search

**Time Complexity:** `O(log(n))`    
**Space Complexity:** `O(1)`

```python
def binary_search(arr, k):
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        mid = (l + r) // 2
        # Keep `k` first while comparing, it's more intuitive.
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1
```

Do not forget **equals** in `<=` at `while l <=r:`.     
Make sure to return `-1` in case you don't find the `k`.

### Common Mistake: Forgetting the `=` in `while l <= r`

**Why it matters:** When `l == r`, you have one unexamined element at that index. If you use `l < r` instead, the loop exits without checking it.

**Single element example:**
```python
arr = [5]
k = 5

# With l < r: Loop never runs → returns -1 ❌
# With l <= r: Checks arr[0], finds it → returns 0 ✓
```

**Memory hook:** *"Equal means examine; less than means leave it."*

Always use `<=` to ensure you check the final middle element before returning -1.

