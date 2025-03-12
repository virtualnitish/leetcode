# 105. Construct Binary Tree from Preorder and Inorder Traversal

## O(n<sup>2</sup>) method, easy to implement

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    # Root value is the first element in preorder traversal
    root_val = preorder.pop(0)
    root = TreeNode(root_val)
    # Find the index of root in inorder traversal
    mid = inorder.index(root_val)
    
    root.left = buildTree(preorder, inorder[:mid])
    root.right = buildTree(preorder, inorder[mid + 1:])
    
    return root

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)
# The constructed binary tree should be:
#        3
#      /   \
#     9    20
#         /  \
#        15   7
```

### Approach:
The core trick here is to use the preorder traversal to determine the root of the tree and use the inorder traversal to determine the left and right subtrees. By recursively applying this method, we can construct the entire tree.

### Time & Space Complexity:
- **Time Complexity:** O(n<sup>2</sup>), where n is the number of nodes in the tree. This is because both `preorder.pop(0)` and `inorder.index(root_val)` are O(n) operations, and they are called for each node in the tree.
- **Space Complexity:** `O(n)`, where n is the size of the input lists. This includes the recursion stack space and the space used by the lists.

---

## `O(n)` Method

```python
def buildTree(preorder, inorder):
    # Create a hash map to store the indices of inorder elements
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    preorder_iter = iter(preorder)  # Use an iterator to avoid pop(0)

    def helper(left, right):
        if left > right:
            return None
        
        # Get the current root value from preorder
        root_val = next(preorder_iter)
        root = TreeNode(root_val)
        
        # Find the index of root in inorder
        mid = inorder_map[root_val]
        
        # Recursively build the left and right subtrees
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        
        return root

    return helper(0, len(inorder) - 1)
```

### Key Optimizations:
1. **Hash Map for Inorder Indices:**
   - Using a dictionary `inorder_map` to store the indices of elements in the `inorder` traversal allows for O(1) lookup time. This eliminates the need to use `inorder.index(root_val)`, which is O(n).

2. **Iterator for Preorder Traversal:**
   - Instead of using `pop(0)` to remove the first element from the `preorder` list (which is O(n) for each call due to list shifting), an iterator `preorder_iter` is used to traverse through the `preorder` list. Using `next(preorder_iter)` allows for O(1) access to the next element.

### Time Complexity:
- **O(n)**:
  - Building the `inorder_map` takes O(n) time.
  - The `helper` function processes each node exactly once, and operations like `next(preorder_iter)` and accessing `inorder_map[root_val]` are O(1).
  - Thus, the overall time complexity is O(n).

### Space Complexity:
- **O(n)**:
  - The `inorder_map` uses O(n) space.
  - The recursion stack uses O(h) space, where `h` is the height of the tree. In the worst case (skewed tree), h = n, so the space complexity is O(n).


### Step-by-Step Visualization:

1. **Initial Preorder and Inorder Traversals:**
   - Preorder: [3, 9, 20, 15, 7]
   - Inorder: [9, 3, 15, 20, 7]
   - `inorder_map` = {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}

2. **First Call:**
   - `left` = 0, `right` = 4
   - `root_val` = 3 (from `preorder_iter`)
   - `inorder_index` = 1 (from `inorder_map`)
   - Create `TreeNode(3)`
   - Build left subtree with `left` = 0, `right` = 0
   - Build right subtree with `left` = 2, `right` = 4

```
        3
```

3. **Second Call (Left Subtree of 3):**
   - `left` = 0, `right` = 0
   - `root_val` = 9 (from `preorder_iter`)
   - `inorder_index` = 0 (from `inorder_map`)
   - Create `TreeNode(9)`
   - Build left subtree with `left` = 0, `right` = -1 (returns None)
   - Build right subtree with `left` = 1, `right` = 0 (returns None)

```
        3
       /
      9
```

4. **Third Call (Right Subtree of 3):**
   - `left` = 2, `right` = 4
   - `root_val` = 20 (from `preorder_iter`)
   - `inorder_index` = 3 (from `inorder_map`)
   - Create `TreeNode(20)`
   - Build left subtree with `left` = 2, `right` = 2
   - Build right subtree with `left` = 4, `right` = 4

```
        3
       / \
      9   20
```

5. **Fourth Call (Left Subtree of 20):**
   - `left` = 2, `right` = 2
   - `root_val` = 15 (from `preorder_iter`)
   - `inorder_index` = 2 (from `inorder_map`)
   - Create `TreeNode(15)`
   - Build left subtree with `left` = 2, `right` = 1 (returns None)
   - Build right subtree with `left` = 3, `right` = 2 (returns None)

```
        3
       / \
      9   20
         /
        15
```

6. **Fifth Call (Right Subtree of 20):**
   - `left` = 4, `right` = 4
   - `root_val` = 7 (from `preorder_iter`)
   - `inorder_index` = 4 (from `inorder_map`)
   - Create `TreeNode(7)`
   - Build left subtree with `left` = 4, `right` = 3 (returns None)
   - Build right subtree with `left` = 5, `right` = 4 (returns None)

```
        3
       / \
      9   20
         /  \
        15   7
```

### Final Binary Tree:
```
        3
       / \
      9   20
         /  \
        15   7
```

In each step, we use the `preorder_iter` to get the current root value and use the `inorder_map` to find the index of the root in the `inorder` traversal. This allows us to efficiently divide the `inorder` list into left and right subtrees and build the binary tree recursively.

---

## Iterative Method

In case your interviewer hates you to his very core!    

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0
        
        for pre_val in preorder[1:]:
            node = stack[-1]
            if node.val != inorder[inorder_index]:
                node.left = TreeNode(pre_val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_index]:
                    node = stack.pop()
                    inorder_index += 1
                node.right = TreeNode(pre_val)
                stack.append(node.right)
                
        return root

```


### **Core Idea**

- **Preorder Traversal** gives us the sequence of nodes in the order they're visited: **root**, then **left**, then **right**.
- **Inorder Traversal** provides the nodes in the left-to-right order: **left**, **root**, **right**.
- By using a **stack**, we can mimic the call stack of a recursive function, allowing us to build the tree iteratively.
- The key is to **determine when to switch from constructing left subtrees to right subtrees**, which we do by comparing the nodes on the stack with the inorder traversal.

---

### **Step-by-Step Explanation Using an Example**

**Let's use an example to illustrate this:**

- **Preorder**: `[3, 9, 20, 15, 7]`
- **Inorder**: `[9, 3, 15, 20, 7]`

We'll build the tree iteratively using these traversals.

#### **Initialization**

1. **Create the root node:**
   - The first element of preorder is `3`, which is the root.
   - Create a `TreeNode` with value `3`.
   - Initialize a stack and push the root onto it.
   - Set `inorder_index` to `0`.

   **State:**
   - **Stack**: `[3]`
   - **Current Node**: `3`
   - **Inorder Index**: `0`

---

#### **Iterate Through Preorder Traversal**

We will now iterate through the rest of the preorder list `[9, 20, 15, 7]`.

---

##### **Iteration 1: `pre_val = 9`**

1. **Peek at the top of the stack (`node = stack[-1]`):**
   - **Node**: `3`

2. **Compare `node.val` with `inorder[inorder_index]`:**
   - `3` (node.val) **≠** `9` (inorder[0])

3. **Since they are different:**
   - This means we're still traversing the left subtree.
   - **Create a left child** of `3` with value `9`.
   - Push `9` onto the stack.

   **State:**
   - **Stack**: `[3, 9]`
   - **Current Node**: `9`
   - **Inorder Index**: `0`

---

##### **Iteration 2: `pre_val = 20`**

1. **Peek at the top of the stack (`node = stack[-1]`):**
   - **Node**: `9`

2. **Compare `node.val` with `inorder[inorder_index]`:**
   - `9` (node.val) **=** `9` (inorder[0])

3. **Since they are equal:**
   - We've finished constructing the left subtree of `9`.
   - **Pop nodes from the stack** while `node.val` equals `inorder[inorder_index]`:
     - Pop `9`, increment `inorder_index` to `1`.
     - Now `node` is `3`, `inorder[inorder_index]` is `3`.
     - Pop `3`, increment `inorder_index` to `2`.
   - **Assign the next node as the right child** of the last popped node (`3`).
   - **Create a right child** of `3` with value `20`.
   - Push `20` onto the stack.

   **State:**
   - **Stack**: `[20]`
   - **Current Node**: `20`
   - **Inorder Index**: `2`

---

##### **Iteration 3: `pre_val = 15`**

1. **Peek at the top of the stack (`node = stack[-1]`):**
   - **Node**: `20`

2. **Compare `node.val` with `inorder[inorder_index]`:**
   - `20` (node.val) **≠** `15` (inorder[2])

3. **Since they are different:**
   - We're building the left subtree of `20`.
   - **Create a left child** of `20` with value `15`.
   - Push `15` onto the stack.

   **State:**
   - **Stack**: `[20, 15]`
   - **Current Node**: `15`
   - **Inorder Index**: `2`

---

##### **Iteration 4: `pre_val = 7`**

1. **Peek at the top of the stack (`node = stack[-1]`):**
   - **Node**: `15`

2. **Compare `node.val` with `inorder[inorder_index]`:**
   - `15` (node.val) **=** `15` (inorder[2])

3. **Since they are equal:**
   - We've finished the left subtree of `15`.
   - **Pop nodes from the stack** while `node.val` equals `inorder[inorder_index]`:
     - Pop `15`, increment `inorder_index` to `3`.
     - Now `node` is `20`, `inorder[inorder_index]` is `20`.
     - Pop `20`, increment `inorder_index` to `4`.
   - **Assign the next node as the right child** of the last popped node (`20`).
   - **Create a right child** of `20` with value `7`.
   - Push `7` onto the stack.

   **State:**
   - **Stack**: `[7]`
   - **Current Node**: `7`
   - **Inorder Index**: `4`

---

#### **Completion**

- **Inorder Index** has reached the length of the inorder list.
- The stack has one node (`7`), which doesn't have any children.
- We've finished iterating through the preorder list.

---

### **Final Binary Tree Structure**

```
      3
     / \
    9   20
        /  \
       15   7
```

---

### **Understanding the Flow**

- We **use the preorder traversal** to decide the **order of node insertion**.
- The **stack** keeps track of nodes whose subtrees we're currently building.
- When the **top of the stack matches the inorder traversal**, it indicates that we've completed the left subtree for that node, and we need to start constructing the right subtree.
- By **popping from the stack**, we backtrack to the correct parent node for the right child.
- We **alternate** between adding left children (when the top of the stack doesn't match inorder) and adding right children (when it does match).

---

### **Breaking Down the Code**

```python
for pre_val in preorder[1:]:
    node = stack[-1]
    if node.val != inorder[inorder_index]:
        # Continue building the left subtree
        node.left = TreeNode(pre_val)
        stack.append(node.left)
    else:
        # Left subtree is complete, backtrack to build right subtree
        while stack and stack[-1].val == inorder[inorder_index]:
            node = stack.pop()
            inorder_index += 1
        node.right = TreeNode(pre_val)
        stack.append(node.right)
```

- **`node = stack[-1]`**: Peek at the current node we're processing.
- **`if node.val != inorder[inorder_index]:`**: If the current node's value isn't the next in inorder traversal, we're building the **left subtree**.
  - **Add a left child**, push it onto the stack.
- **`else:`**: If it matches, we've completed the left subtree, and need to construct the **right subtree**.
  - **Pop nodes** from the stack while they match the inorder traversal (backtracking).
  - **Add a right child** to the last unmatched node, push it onto the stack.
- **`inorder_index`**: Keeps track of our position in the inorder traversal.

---

### **Key Takeaways**

- **Simulating Recursion**: The stack acts similarly to the call stack in recursion, helping us keep track of where we are in the tree.
- **Left Subtrees First**: We always attempt to build the left subtree until we can't go further.
- **Backtracking**: When we encounter nodes matching the inorder traversal, we backtrack to find where to insert the right child.
- **Synchronization**: By comparing `node.val` with `inorder[inorder_index]`, we synchronize the preorder and inorder traversals to build the tree accurately.

---

### **Why This Works**

- **Preorder traversal** always visits nodes in the order: **root**, then **left subtree**, then **right subtree**.
- **Inorder traversal** visits nodes in the order: **left subtree**, **root**, then **right subtree**.
- By using both traversals together, we can determine when we've finished constructing a node's left subtree (when `node.val` matches `inorder[inorder_index]`) and need to start building the right subtree.

---

### **Visual Summary Using ASCII Diagram**

```
Preorder: [3, 9, 20, 15, 7]
Inorder:  [9, 3, 15, 20, 7]

Construct Tree:

1. Root is 3 (from Preorder)
   - Stack: [3]
2. Next Preorder value: 9
   - 3 != inorder[0] (9)
   - Add 9 as left child of 3
   - Stack: [3, 9]
3. Next Preorder value: 20
   - Node 9 == inorder[0] (9)
     - Pop 9, inorder_index = 1
   - Node 3 == inorder[1] (3)
     - Pop 3, inorder_index = 2
   - Add 20 as right child of 3
   - Stack: [20]
4. Next Preorder value: 15
   - 20 != inorder[2] (15)
   - Add 15 as left child of 20
   - Stack: [20, 15]
5. Next Preorder value: 7
   - Node 15 == inorder[2] (15)
     - Pop 15, inorder_index = 3
   - Node 20 == inorder[3] (20)
     - Pop 20, inorder_index = 4
   - Add 7 as right child of 20
   - Stack: [7]
```

---

### **In Conclusion**

The iterative method is all about **using a stack to keep track of nodes** and **comparing the current node with the inorder traversal** to decide when to switch from constructing left subtrees to right subtrees.

- **Left Child Addition**: When the stack's top node doesn't match the current inorder value, we add a left child.
- **Right Child Addition**: When the stack's top node matches the inorder value, we pop nodes (backtracking) until we find the correct parent for the right child.

This approach effectively mirrors the recursive construction, but manages the traversal and construction process explicitly using a stack.

---

Feel free to ask if you have any more questions or need further clarification on any part of the process! I'm here to help you grasp the concept fully. 😊