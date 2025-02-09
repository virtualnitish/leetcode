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
- **Time Complexity:** `O(n^2)`, where n is the number of nodes in the tree. This is because both `preorder.pop(0)` and `inorder.index(root_val)` are O(n) operations, and they are called for each node in the tree.
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

