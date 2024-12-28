"""Test module for Trees algorithms."""

import pytest

from src.trees import TreeNode, bfs, dfs


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3]),
        (TreeNode(1, None, TreeNode(2, TreeNode(3))), [1, 2, 3]),
        (TreeNode(1, TreeNode(2, TreeNode(3)), None), [1, 2, 3]),
        (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4)), [1, 2, 3, 4]),
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), None),
                TreeNode(3, None, TreeNode(5, TreeNode(6))),
            ),
            [1, 2, 4, 3, 5, 6],
        ),
    ],
)
def test_dfs(root: TreeNode, expected: list[int]):
    assert dfs(root) == expected


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3]),
        (TreeNode(1, None, TreeNode(2, TreeNode(3))), [1, 2, 3]),
        (TreeNode(1, TreeNode(2, TreeNode(3)), None), [1, 2, 3]),
        (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4)), [1, 2, 4, 3]),
        (
            TreeNode(
                1,
                TreeNode(2, TreeNode(4), None),
                TreeNode(3, None, TreeNode(5, TreeNode(6))),
            ),
            [1, 2, 3, 4, 5, 6],
        ),
    ],
)
def test_bfs(root: TreeNode, expected: list[int]):
    assert bfs(root) == expected


if __name__ == "__main__":
    pytest.main()
