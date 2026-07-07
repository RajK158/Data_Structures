from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(min_heap, [dist, x, y])

        res = []

        for _ in range(k):
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.kClosest([[0,2],[2,2]], 1))
    print(sol.kClosest([[0,2],[2,0],[2,2]], 2))