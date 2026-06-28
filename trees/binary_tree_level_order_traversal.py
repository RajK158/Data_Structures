# Problem: Binary Tree Level Order Traversal
# Pattern: BFS
# Time: O(n)
# Space: O(n)

from collections import deque

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root):

        if not root:
            return []

        res = []
        q = deque([root])

        while q:

            level = []

            for _ in range(len(q)):

                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level)

        return res


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

    print(sol.levelOrder(root))