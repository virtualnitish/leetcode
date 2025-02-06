# Trees

## DFS 

**Time Complexity:** O(n)    
**Space Complexity:**    
                    - Best case: O(log(n)) because max height of a tree is log(n)    
                    - Worst case: O(n)   


### Iterative Method using Stack

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Pre-order (root, left, right)
def dfs_preorder(root):
    if root is None:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


# In-order (left, root, right)
# Change the traversal order to visit the left child first, then the root, and then the right child.
def dfs_inorder(root):
    if root is None:
        return []
    stack, result = [], []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

# Post-order (left, right, root)
# Modify the final result list by reversing it to get the correct post-order traversal.
def dfs_postorder(root):
    if root is None:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]
```


### Recursive Method

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Pre-order (root, left, right)
def preorder(root):
    result = []
    def helper(node):
        if not node:
            return
        result.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return result

# In-order (left, root, right)
def inorder(root):
    result = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    helper(root)
    return result

# Post-order (left, right, root)
def postorder(root):
    result = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        helper(node.right)
        result.append(node.val)
    helper(root)
    return result

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Pre-order:", preorder(root))
print("In-order:", inorder(root))
print("Post-order:", postorder(root))

```