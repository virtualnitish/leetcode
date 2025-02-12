# Misc. Algorithms

---

# Arrays

## Kadane's Algorithm

Kadane's Algorithm is best known for finding 
the **maximum sum of a contiguous subarray** in `O(n)` time.

```python
def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum+nums[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum
```

`curr_sum = max(nums[i], curr_sum+nums[i])` is the most important part of this code.

