# Problem: Count Good Nodes in Binary Tree
# Pattern: DFS
# Time: O(n)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes(self, root) -> int:

        def dfs(node, max_so_far):

            if not node:
                return 0

            count = 0

            if node.val >= max_so_far:
                count = 1

            max_so_far = max(max_so_far, node.val)

            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)

            return count

        return dfs(root, root.val)


if __name__ == "__main__":

    root = TreeNode(
        2,
        TreeNode(
            1,
            TreeNode(3),
            None
        ),
        TreeNode(
            1,
            TreeNode(1),
            TreeNode(5)
        )
    )

    sol = Solution()

    print(sol.goodNodes(root))  # 3