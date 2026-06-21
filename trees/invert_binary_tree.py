# Problem: Invert Binary Tree
# Pattern: DFS / Recursion
# Time: O(n)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root):

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


def preorder(root):

    if not root:
        return

    print(root.val, end=" ")

    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":

    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(5)
        ),
        TreeNode(
            3,
            TreeNode(6),
            TreeNode(7)
        )
    )

    sol = Solution()

    inverted = sol.invertTree(root)

    preorder(inverted)