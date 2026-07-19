"""
==========================================
Binary Tree - Level Order Traversal (BFS)
==========================================

This program demonstrates Level Order
Traversal (Breadth-First Search) of a
Binary Tree using a Queue.

Traversal:
- Level Order (BFS)
"""

from collections import deque
from typing import Optional


class TreeNode:
    """Represents a node in a Binary Tree."""

    def __init__(self, data: int):
        self.data = data
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class BinaryTree:
    """Binary Tree implementation with BFS traversal."""

    def __init__(self):
        self.root: Optional[TreeNode] = None

    # --------------------------------------
    # Level Order Traversal (BFS)
    # --------------------------------------

    def level_order(self) -> None:

        if self.root is None:
            print("Tree is empty.")
            return

        queue = deque([self.root])

        while queue:

            current = queue.popleft()

            print(current.data, end=" ")

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    tree = BinaryTree()

    # Build Binary Tree

    tree.root = TreeNode(10)

    tree.root.left = TreeNode(20)
    tree.root.right = TreeNode(30)

    tree.root.left.left = TreeNode(40)
    tree.root.left.right = TreeNode(50)

    tree.root.right.right = TreeNode(60)

    print("Level Order Traversal (BFS):")

    tree.level_order()

    print()


if __name__ == "__main__":
    main()
