from typing import List
from collections import deque


class Solution:

    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> List[int]:

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for nxt in graph[course]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)

        if len(order) == numCourses:
            return order

        return []


if __name__ == "__main__":
    sol = Solution()

    print(sol.findOrder(3, [[1, 0]]))
    print(sol.findOrder(3, [[0, 1], [1, 2], [2, 0]]))
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))