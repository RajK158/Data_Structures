# Problem: Valid Binary Search Tree
# Pattern: DFS + Bounds
# Time: O(n)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root):

        def dfs(node, left, right):

            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (
                dfs(node.left, left, node.val)
                and
                dfs(node.right, node.val, right)
            )

        return dfs(root, float("-inf"), float("inf"))


if __name__ == "__main__":

    # Valid BST
    root1 = TreeNode(
        2,
        TreeNode(1),
        TreeNode(3)
    )

    # Invalid BST
    root2 = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    sol = Solution()

    print(sol.isValidBST(root1))  # True
    print(sol.isValidBST(root2))  # False