# Problem: Kth Smallest Integer in BST
# Pattern: Iterative Inorder Traversal
# Time: O(h + k)
# Space: O(h)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root, k: int) -> int:

        stack = []
        curr = root

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val

            curr = curr.right


if __name__ == "__main__":

    # Tree 1
    #      2
    #     / \
    #    1   3

    root1 = TreeNode(
        2,
        TreeNode(1),
        TreeNode(3)
    )

    # Tree 2
    #      4
    #     / \
    #    3   5
    #   /
    #  2

    root2 = TreeNode(
        4,
        TreeNode(
            3,
            TreeNode(2),
            None
        ),
        TreeNode(5)
    )

    sol = Solution()

    print(sol.kthSmallest(root1, 1))  # 1
    print(sol.kthSmallest(root2, 4))  # 5