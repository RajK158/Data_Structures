# Problem: Course Schedule
# Pattern: Graph / DFS / Cycle Detection
# Time: O(V + E)
# Space: O(V + E)

from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)

        visiting = set()
        visited = set()

        def dfs(course):

            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


if __name__ == "__main__":

    sol = Solution()

    print(sol.canFinish(2, [[0,1]]))          # True
    print(sol.canFinish(2, [[0,1],[1,0]]))    # False
    print(sol.canFinish(4, [[1,0],[2,1],[3,2]]))  # True