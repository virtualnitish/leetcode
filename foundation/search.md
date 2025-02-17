# Search

## Binary Search

**Time Complexity:** O(log(n))    
**Space Complexity:** O(1)

```python
def binary_search(arr, k):
    l = 0
    r = n - 1
    
    while l <= r:
        mid = (l + r) // 2
        if k == arr[mid]:
            return mid
        elif k < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1
```

Do not forget the `<=` in `while l <=r:`.     
Make sure to return `-1` in case you don't find the `k`.