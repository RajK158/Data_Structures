# Problem: Construct Binary Tree from Preorder and Inorder Traversal
# Pattern: DFS / Recursion
# Time: O(n)
# Space: O(n)

from typing import List

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]):

        inorder_index = {}

        for i, val in enumerate(inorder):
            inorder_index[val] = i

        self.pre_idx = 0

        def dfs(left, right):

            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            mid = inorder_index[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)


def preorder_print(root):

    if not root:
        return

    print(root.val, end=" ")
    preorder_print(root.left)
    preorder_print(root.right)


if __name__ == "__main__":

    sol = Solution()

    root = sol.buildTree(
        [1,2,3,4],
        [2,1,3,4]
    )

    preorder_print(root)