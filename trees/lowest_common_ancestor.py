# Problem: Lowest Common Ancestor in BST
# Pattern: Binary Search Tree
# Time: O(h)
# Space: O(1)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def lowestCommonAncestor(self, root, p, q):

        curr = root

        while curr:

            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            else:
                return curr


if __name__ == "__main__":

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node5.left = node3
    node5.right = node8
    node3.left = node1
    node3.right = node4
    node1.right = node2
    node8.left = node7
    node8.right = node9

    sol = Solution()

    print(sol.lowestCommonAncestor(node5, node3, node8).val)  # 5
    print(sol.lowestCommonAncestor(node5, node3, node4).val)  # 3