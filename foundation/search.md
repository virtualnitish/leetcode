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