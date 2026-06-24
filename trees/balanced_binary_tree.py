# Problem: Balanced Binary Tree
# Pattern: DFS
# Time: O(n)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root):

        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return dfs(root) != -1


if __name__ == "__main__":

    root1 = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            None
        )
    )

    root2 = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                5
            ),
            None
        ),
        TreeNode(
            3,
            TreeNode(4),
            None
        )
    )

    sol = Solution()

    print(sol.isBalanced(root1))  # True
    print(sol.isBalanced(root2))  # False