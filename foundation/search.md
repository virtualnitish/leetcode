# Search

## Binary Search

**Time Complexity:** O(log(n))    
**Space Complexity:** O(1)

```python
def binary_search(self, arr, n, k):
    start = 0
    end = n - 1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == k:
            return mid
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
```