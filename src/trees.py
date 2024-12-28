"""Implementation of common algorithms for Trees."""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: Optional[TreeNode]) -> list[int]:
    """Depth-first search implementation. The function traverses the tree in a depth-first manner.

    Args:
        root (TreeNode): Root of the tree to traverse.

    Returns:
        list[int]: List of tree nodes in the order they were visited.
    """

    if not root:
        return []

    return [root.val] + dfs(root.left) + dfs(root.right)


def bfs(root: Optional[TreeNode]) -> list[int]:
    """Breadth-first search implementation. The function traverses the tree in a breadth-first manner.

    Args:
        root (TreeNode): Root of the tree to traverse.

    Returns:
        list[int]: List of tree nodes in the order they were visited.
    """

    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
