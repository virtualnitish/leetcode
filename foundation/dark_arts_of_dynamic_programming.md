# Dark Arts of Dynamic Programming

![The Black Book of Dynamic Programming](images/dark_arts_of_dynamic_programming-image-1.png)


### **Dynamic Programming Template**

```python
def dp_problem_solver(data):
    # Base cases
    if not data:
        return base_case_value

    # Initialize DP array or variables
    dp = [initial_values]  # For problems requiring an array
    # Or use variables for optimized space
    prev = initial_prev_value
    curr = initial_curr_value

    # Iterate through the data
    for item in data:
        # Compute the optimal value at each step
        # For array-based DP
        dp[i] = optimal_function(dp, i)
        # For space-optimized DP
        new_curr = max_function(prev, curr, item)
        prev = curr
        curr = new_curr

    # Return the result
    return dp[-1]  # Or curr, depending on the approach

# Example usage
data = [...]  # Input data specific to the problem
print(dp_problem_solver(data))
```

**Key Components:**

- **Base Cases:** Handle scenarios where the input is empty or has minimal elements.
- **Initialization:** Set up a DP array or variables to store computed values.
- **State Transition (Recurrence Relation):** Define how to compute the current state based on previous states.
- **Iteration:** Loop through the input, updating the DP array or variables.
- **Result Retrieval:** Extract the final result from the DP array or variables.

---

### **Applying the Template to "House Robber"**

```python
def rob(nums):
    # Base cases
    if not nums:
        return 0

    # Initialization of variables
    prev = 0  # Max profit up to house i-2
    curr = 0  # Max profit up to house i-1

    # Iterate through the list of houses
    for num in nums:
        # Calculate the new maximum profit
        new_curr = max(prev + num, curr)
        # Update previous profits for next iteration
        prev = curr
        curr = new_curr

    # The current maximum profit is the answer
    return curr

# Example usage
houses = [2, 7, 9, 3, 1]
print(rob(houses))  # Output: 12
```

**Explanation:**

- **State Definition:** At each step, `curr` holds the maximum profit up to the current house, and `prev` holds the maximum profit up to the previous house.
- **Recurrence Relation:** `new_curr = max(prev + num, curr)`
  - **Rob Current House:** `prev + num` (can't rob the previous house)
  - **Skip Current House:** `curr` (keep the maximum profit so far)
- **Iteration:** Update `prev` and `curr` as we move through each house.
- **Result:** After processing all houses, `curr` contains the maximum profit achievable.

---

### **Other DP Questions in This Category**

These problems share similarities in their DP approach:

1. **53. Maximum Subarray**
   - **Problem:** Find the contiguous subarray with the largest sum.
   - **Approach:** At each position, decide whether to include the current element in the existing subarray or start a new subarray.

2. **70. Climbing Stairs**
   - **Problem:** Count the number of distinct ways to reach the top of the stairs.
   - **Approach:** The number of ways to reach step `n` is the sum of ways to reach steps `n-1` and `n-2`.

3. **121. Best Time to Buy and Sell Stock**
   - **Problem:** Maximize profit by choosing a single day to buy and a different day to sell.
   - **Approach:** Track the minimum price so far and the maximum profit at each step.

4. **213. House Robber II**
   - **Problem:** Houses are in a circle; first and last houses are adjacent.
   - **Approach:** Run the House Robber algorithm twice, excluding the first house once and the last house once.

5. **276. Paint Fence**
   - **Problem:** Ways to paint a fence with `n` posts using `k` colors without having more than two adjacent posts with the same color.
   - **Approach:** Use DP to track same-color and different-color counts.

6. **91. Decode Ways**
   - **Problem:** Count the number of ways to decode a message encoded as numbers.
   - **Approach:** DP with considerations for valid single and two-digit decodings.

7. **746. Min Cost Climbing Stairs**
   - **Problem:** Minimum cost to reach the top of the floor.
   - **Approach:** At each step, decide to take one or two steps based on minimal accumulated cost.

8. **152. Maximum Product Subarray**
   - **Problem:** Find the contiguous subarray with the largest product.
   - **Approach:** Keep track of maximum and minimum products due to negative numbers.

9. **62. Unique Paths**
   - **Problem:** Count the number of unique paths in a grid from top-left to bottom-right.
   - **Approach:** DP with the sum of ways from the cell above and the cell to the left.

10. **198. House Robber** (Original problem)

---

### **Understanding the Common Pattern**

These problems often require:

- **Decision Making at Each Step:** Choose between multiple options to optimize a certain value.
- **Use of Previous Computations:** Current decision depends on previous results.
- **Optimization Goal:** Maximize or minimize a value (profit, cost, paths).

---

### **Creating Your Own DP Solutions**

When tackling similar DP problems:

1. **Identify the Problem Type:**
   - Is it about maximizing/minimizing a value?
   - Does it involve counting the number of ways?

2. **Define the State:**
   - Determine what each state (element in DP array or variable) represents.
   - For example, `dp[i]` could represent the maximum profit up to house `i`.

3. **Establish the Recurrence Relation:**
   - How does the current state relate to previous states?
   - Formulate the relation based on the problem's constraints.

4. **Determine Base Cases:**
   - Initialize your DP array or variables to handle the smallest subproblems.

5. **Optimize Space if Possible:**
   - If only a few previous states are needed, use variables instead of an array.

6. **Iterate and Compute:**
   - Loop through the input data, updating your states accordingly.

---

### **Additional DP Problems to Explore**

- **221. Maximal Square**
  - Find the largest square containing only 1's in a binary matrix.

- **55. Jump Game**
  - Determine if you can reach the last index of an array.

- **300. Longest Increasing Subsequence**
  - Find the length of the longest increasing subsequence in an array.

- **1143. Longest Common Subsequence**
  - Compute the length of the longest common subsequence between two strings.

- **139. Word Break**
  - Determine if a string can be segmented into space-separated words from a dictionary.

---

### **Going Deeper**

To enhance your DP skills:

- **Practice Pattern Recognition:**
  - Group problems by their DP patterns (e.g., linear sequences, grids, subsets).

- **Study Different DP Approaches:**
  - **Top-Down (Memoization):** Recursive approach with caching.
  - **Bottom-Up (Tabulation):** Iterative approach filling up the DP table.

- **Analyze Time and Space Complexity:**
  - Understand how your DP solution scales with input size.

- **Implement Variations:**
  - Try modifying problems or constraints to see how your DP solution adapts.



## Dynamic Programming Patterns & Templates

### 1. Top-Down (Memoization)
```python
from functools import lru_cache

def top_down_template():
    @lru_cache(maxsize=None)
    def dp(state):
        # Base case
        if base_case_condition:
            return base_case_value
        
        # State transitions
        result = combine_options(dp(next_state1), dp(next_state2))
        return result
    
    return dp(initial_state)

# Example: Fibonacci Number
def fib(n):
    @lru_cache(maxsize=None)
    def dp(i):
        if i <= 1: return i
        return dp(i-1) + dp(i-2)
    return dp(n)
```

### 2. Bottom-Up (Tabulation)
```python
def bottom_up_template():
    n = ...  # problem size
    dp = [0] * (n+1)
    dp[0] = base_case  # Initialize base case
    
    for i in range(1, n+1):
        dp[i] = combine_options(dp[previous_states])
    
    return dp[n]

# Example: Climbing Stairs
def climbStairs(n):
    if n == 1: return 1
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### 3. State Machine
```python
def state_machine_template():
    n = ...  # problem size
    # Initialize state arrays
    state1 = [0]*n
    state2 = [0]*n
    
    # Base cases
    state1[0] = ...
    state2[0] = ...
    
    for i in range(1, n):
        state1[i] = max(state1[i-1], state2[i-1] + ...)
        state2[i] = max(state2[i-1], state1[i-1] - ...)
    
    return max(state1[-1], state2[-1])

# Example: Best Time to Buy/Sell Stock with Cooldown
def maxProfit(prices):
    if not prices: return 0
    n = len(prices)
    hold, sold, rest = [0]*n, [0]*n, [0]*n
    hold[0] = -prices[0]
    for i in range(1, n):
        hold[i] = max(hold[i-1], rest[i-1] - prices[i])
        sold[i] = hold[i-1] + prices[i]
        rest[i] = max(rest[i-1], sold[i-1])
    return max(sold[-1], rest[-1])
```

### 4. 0/1 Knapsack
```python
def knapsack_template():
    weights = [...]
    values = [...]
    capacity = ...
    n = len(weights)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
    
    return dp[n][capacity]

# Space optimized version (1D array)
def knapsack_01(weights, values, capacity):
    dp = [0]*(capacity+1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i]-1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[capacity]
```

### 5. Longest Common Subsequence (LCS)
```python
def LCS_template(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Example usage matches exactly with standard LCS problem
```

### 6. Matrix DP (Grid Problems)
```python
def matrix_dp_template(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    
    # Initialize first row/column
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[m-1][n-1]

# Example: Minimum Path Sum (exactly matches template)
```

### 7. Interval DP
```python
def interval_dp_template():
    nums = [...]  # typically array of numbers
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    
    # Base cases (length = 1)
    for i in range(n):
        dp[i][i] = base_case_value
    
    # Fill for lengths from 2 to n
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = max(min) over all k between i and j of:
                dp[i][k] + dp[k+1][j] + combine_cost
    
    return dp[0][n-1]

# Example: Matrix Chain Multiplication
def matrixChainMultiplication(matrices):
    n = len(matrices)
    dp = [[0]*n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrices[i][0]*matrices[k][1]*matrices[j][1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]
```

### 8. Bitmask DP
```python
def bitmask_dp_template():
    n = ...  # number of elements
    all_mask = (1 << n) - 1
    dp = [[inf] * (1 << n) for _ in range(n)]
    
    # Initialize base cases
    for i in range(n):
        dp[i][1 << i] = 0
    
    # Iterate over all masks
    for mask in range(1 << n):
        for curr in range(n):
            if not (mask & (1 << curr)):
                continue
            for next_node in range(n):
                if not (mask & (1 << next_node)):
                    dp[next_node][mask | (1 << next_node)] = min(
                        dp[next_node][mask | (1 << next_node)],
                        dp[curr][mask] + distance[curr][next_node]
                    )
    
    # Find minimum cost for all nodes visited
    return min(dp[i][all_mask] for i in range(n))

# Example: Traveling Salesman Problem (TSP)
```

### 9. Digit DP
```python
def digit_dp_template(limit):
    s = str(limit)
    n = len(s)
    
    @lru_cache(maxsize=None)
    def dp(pos, tight, leading_zero, ...other_state_params):
        if pos == n:
            return 1 if valid_state else 0
        
        limit = int(s[pos]) if tight else 9
        res = 0
        for d in range(0, limit+1):
            new_tight = tight and (d == limit)
            new_leading_zero = leading_zero and (d == 0)
            
            if ...:  # some condition based on problem
                continue
            
            res += dp(pos+1, new_tight, new_leading_zero, ...new_state_params)
        return res
    
    return dp(0, True, True, ...initial_state)

# Example: Count Numbers with Unique Digits
# (Complex implementation that's too long to show here)
```

### 10. Tree DP
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_dp_template(root):
    def postorder(node):
        if not node:
            return base_case_value
        
        left = postorder(node.left)
        right = postorder(node.right)
        
        # Combine results from left and right
        result = max(left + right + node.val, ...)
        return result
    
    return postorder(root)

# Example: Binary Tree Maximum Path Sum
def maxPathSum(root):
    max_sum = -float('inf')
    def postorder(node):
        nonlocal max_sum
        if not node: return 0
        left = max(postorder(node.left), 0)
        right = max(postorder(node.right), 0)
        max_sum = max(max_sum, left + right + node.val)
        return node.val + max(left, right)
    postorder(root)
    return max_sum
```

**Key Observations:**
1. DP problems often involve making optimal decisions at each step
2. State definition is crucial - what parameters define a subproblem?
3. Look for overlapping subproblems and optimal substructure
4. Start with brute force approach, then add memoization
5. For space optimization, consider if previous states can be discarded

**Common Optimization Techniques:**
- Convert top-down to bottom-up for better space efficiency
- Use rolling arrays (e.g., in knapsack problems)
- Compress state parameters where possible
- Prune unnecessary state transitions

Practice these patterns with problems like:
- Coin Change (Knapsack)
- Longest Increasing Subsequence
- Edit Distance
- Decode Ways
- Word Break
- House Robber
- Partition Equal Subset Sum
