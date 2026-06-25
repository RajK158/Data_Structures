# Problem: Same Binary Tree
# Pattern: DFS / Recursion
# Time: O(n)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )


if __name__ == "__main__":

    # Tree 1
    p = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    # Tree 2
    q = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    # Tree 3
    r = TreeNode(
        1,
        TreeNode(3),
        TreeNode(2)
    )

    sol = Solution()

    print(sol.isSameTree(p, q))  # True
    print(sol.isSameTree(p, r))  # False