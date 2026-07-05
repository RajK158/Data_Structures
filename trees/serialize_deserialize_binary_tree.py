# Problem: Serialize and Deserialize Binary Tree
# Pattern: DFS / Preorder
# Time: O(n)
# Space: O(n)

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


def preorder(root):
    if not root:
        print("N", end=" ")
        return

    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":

    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5)
        )
    )

    codec = Codec()

    data = codec.serialize(root)
    print(data)

    new_root = codec.deserialize(data)
    preorder(new_root)