# Problem: Diameter of Binary Tree
# Pattern: DFS
# Time: O(n)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root):

        self.res = 0

        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.res


if __name__ == "__main__":

    root = TreeNode(
        1,
        None,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(5),
                None
            ),
            TreeNode(4)
        )
    )

    sol = Solution()

    print(sol.diameterOfBinaryTree(root))  # 3