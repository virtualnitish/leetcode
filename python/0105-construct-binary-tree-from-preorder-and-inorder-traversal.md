# 105. Construct Binary Tree from Preorder and Inorder Traversal

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
    inorder_index = inorder.index(root_val)
    
    root.left = buildTree(preorder, inorder[:inorder_index])
    root.right = buildTree(preorder, inorder[inorder_index + 1:])
    
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
- **Time Complexity:** `O(n)`, where n is the number of nodes in the tree. Each node is processed once.
- **Space Complexity:** `O(n)`, where n is the size of the input lists. This includes the recursion stack space and the space used by the lists.
