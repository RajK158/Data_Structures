# Problem: Kth Largest Element in an Array
# Pattern: Min Heap
# Time: O(n log k)
# Space: O(k)

from typing import List
import heapq

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []

        for n in nums:
            heapq.heappush(min_heap, n)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


if __name__ == "__main__":

    sol = Solution()

    print(sol.findKthLargest([2,3,1,5,4], 2))        # 4
    print(sol.findKthLargest([2,3,1,1,5,5,4], 3))    # 4