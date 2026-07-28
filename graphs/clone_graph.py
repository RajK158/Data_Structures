# Problem: Clone Graph
# Pattern: Graph / DFS
# Time: O(V + E)
# Space: O(V)

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:

    def cloneGraph(self, node):

        if not node:
            return None

        old_to_new = {}

        def dfs(cur):

            if cur in old_to_new:
                return old_to_new[cur]

            copy = Node(cur.val)
            old_to_new[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)


if __name__ == "__main__":

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.neighbors = [n2]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2]

    sol = Solution()

    clone = sol.cloneGraph(n1)

    print(clone.val)
    print([x.val for x in clone.neighbors])
    print([x.val for x in clone.neighbors[0].neighbors])