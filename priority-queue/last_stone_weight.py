# Problem: Last Stone Weight
# Pattern: Max Heap
# Time: O(n log n)
# Space: O(n)

from typing import List
import heapq

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            if first != second:
                heapq.heappush(max_heap, -(first - second))

        return -max_heap[0] if max_heap else 0


if __name__ == "__main__":

    sol = Solution()

    print(sol.lastStoneWeight([2,3,6,2,4]))  # 1
    print(sol.lastStoneWeight([1,2]))        # 1