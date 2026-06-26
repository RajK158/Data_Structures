# Problem: Subtree of Another Tree
# Pattern: DFS
# Time: O(n * m)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, root, subRoot) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.sameTree(p.left, q.left)
            and
            self.sameTree(p.right, q.right)
        )


if __name__ == "__main__":

    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(5)
        ),
        TreeNode(3)
    )

    subRoot = TreeNode(
        2,
        TreeNode(4),
        TreeNode(5)
    )

    sol = Solution()

    print(sol.isSubtree(root, subRoot))  # True