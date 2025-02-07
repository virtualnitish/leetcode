# Sort

## Merge Sort

- **Time Complexity:** O(n log(n))
- **Space Complexity:**
  - **Best case:** O(n) auxiliary space
  - **Worst case:** O(n) auxiliary space


```python
class Solution:
    def merge(self, arr, l, m, r): 
        ## Create copy of arr
        left_arr = arr[l:m+1]
        right_arr = arr[m+1:r+1]
        
        i = 0
        j = 0
        k = l
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
                    
    def mergeSort(self, arr, l, r):
        if l == r:
            return
        
        mid = (r + l) // 2
        
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        
        self.merge(arr, l, mid, r)

# Example Usage
solution = Solution()
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
solution.mergeSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
```