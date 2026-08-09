from typing import List


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):

            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        def union(a, b):

            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []


if __name__ == "__main__":

    sol = Solution()

    print(sol.findRedundantConnection(
        [[1,2], [1,3], [3,4], [2,4]]
    ))

    print(sol.findRedundantConnection(
        [[1,2], [1,3], [1,4], [3,4], [4,5]]
    ))