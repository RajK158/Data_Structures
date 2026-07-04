# Problem: Binary Tree Maximum Path Sum
# Pattern: DFS
# Time: O(n)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root) -> int:

        self.res = root.val

        def dfs(node):

            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.res = max(self.res, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)

        return self.res


if __name__ == "__main__":

    root1 = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    root2 = TreeNode(
        -15,
        TreeNode(10),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(5)
        )
    )

    sol = Solution()

    print(sol.maxPathSum(root1))  # 6
    print(sol.maxPathSum(root2))  # 40