from typing import List


class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):

            visited.add(node)

            for nei in graph[node]:

                if nei == parent:
                    continue

                if nei in visited:
                    return False

                if not dfs(nei, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n


if __name__ == "__main__":

    sol = Solution()

    print(sol.validTree(
        5,
        [[0,1], [0,2], [0,3], [1,4]]
    ))  # True

    print(sol.validTree(
        5,
        [[0,1], [1,2], [2,3], [1,3], [1,4]]
    ))  # False

    print(sol.validTree(
        4,
        [[0,1], [2,3]]
    ))  # False