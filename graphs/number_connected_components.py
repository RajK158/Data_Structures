from typing import List


class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = list(range(n))
        size = [1] * n

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

        components = n

        for a, b in edges:
            if union(a, b):
                components -= 1

        return components


if __name__ == "__main__":

    sol = Solution()

    print(sol.countComponents(
        5,
        [[0,1], [1,2], [3,4]]
    ))  # 2

    print(sol.countComponents(
        5,
        [[0,1], [1,2], [2,3], [3,4]]
    ))  # 1

    print(sol.countComponents(
        5,
        []
    ))  