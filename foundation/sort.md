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

