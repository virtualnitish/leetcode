# Binary Search Trees

## Key Points for Solving BST Problems on Leetcode:

### 1. **Understanding BST Properties**
- **Node Relationships**: Remember that for any node, all nodes in its left subtree are smaller, and all nodes in its right subtree are larger.
- **Inorder Traversal**: An inorder traversal of a BST yields the nodes in ascending order.

### 2. **Types of Traversals**
- **Inorder Traversal**: Used to retrieve nodes in ascending order.
- **Preorder Traversal**: Useful for creating a copy of the tree.
- **Postorder Traversal**: Often used for deleting a tree.

### 3. **Common Operations**
- **Insertion**: Always ensure to maintain the BST property after inserting a node.
- **Deletion**: Handle the three main cases (leaf node, node with one child, node with two children) correctly to maintain the BST property.
- **Searching**: Leverage the BST property to efficiently search for a node, resulting in an average time complexity of O(log n).

### 4. **Optimization Techniques**
- **Balancing**: Consider AVL trees or Red-Black trees if balancing is needed to maintain optimal search times.
- **Iterative vs. Recursive**: Choose between iterative and recursive approaches based on space complexity constraints.

### 5. **Edge Cases**
- **Empty Trees**: Always check if the tree is empty at the start of operations.
- **Single Node**: Handle operations for trees with a single node separately.
- **Imbalanced Trees**: Ensure your solution performs well even with highly imbalanced trees.

### 6. **Memory Management**
- **Recursive Calls**: Be mindful of the call stack size in recursive approaches to avoid stack overflow with large trees.
- **Auxiliary Data Structures**: Use additional data structures like stacks or queues judiciously to manage space complexity.

### 7. **Code Readability and Efficiency**
- **Clarity**: Write clear, concise, and well-commented code. This makes debugging and understanding easier.
- **Efficiency**: Aim for optimal time and space complexity. Consider the worst-case scenarios.

### Example: Inorder Traversal of a BST
```python
def inorder_traversal(root):
    res = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res
```
