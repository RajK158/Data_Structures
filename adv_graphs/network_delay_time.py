from typing import List
import heapq


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = {i: [] for i in range(1, n + 1)}

        for u, v, t in times:
            graph[u].append((v, t))

        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:

            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = max(max_time, time)

            for nei, weight in graph[node]:

                if nei not in visited:
                    heapq.heappush(
                        min_heap,
                        (time + weight, nei)
                    )

        if len(visited) == n:
            return max_time

        return -1


if __name__ == "__main__":

    sol = Solution()

    print(sol.networkDelayTime(
        [[1,2,1], [2,3,1], [1,4,4], [3,4,1]],
        4,
        1
    ))  # 3

    print(sol.networkDelayTime(
        [[1,2,1], [2,3,1]],
        3,
        2
    ))  # -1