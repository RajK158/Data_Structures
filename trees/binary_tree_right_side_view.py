# Problem: Binary Tree Right Side View
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

    def rightSideView(self, root):

        if not root:
            return []

        res = []
        q = deque([root])

        while q:

            right_side = None

            for _ in range(len(q)):

                node = q.popleft()
                right_side = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(right_side.val)

        return res


if __name__ == "__main__":

    root = TreeNode(
        1,
        TreeNode(
            2,
            None,
            TreeNode(4)
        ),
        TreeNode(
            3,
            None,
            TreeNode(5)
        )
    )

    sol = Solution()

    print(sol.rightSideView(root))