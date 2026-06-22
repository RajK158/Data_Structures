# Problem: Maximum Depth of Binary Tree
# Pattern: DFS / Recursion
# Time: O(n)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root):

        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )


if __name__ == "__main__":

    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            None
        )
    )

    sol = Solution()

    print(sol.maxDepth(root))  # 3