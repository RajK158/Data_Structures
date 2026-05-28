# Problem: Sliding Window Maximum
# Pattern: Monotonic Deque
# Time: O(n)
# Space: O(k)

from typing import List
from collections import deque

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque()
        res = []

        l = 0

        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.maxSlidingWindow([1,2,1,0,4,2,6], 3))  # [2,2,4,4,6]
    print(sol.maxSlidingWindow([1], 1))              # [1]
    print(sol.maxSlidingWindow([9,8,7,6], 2))        # [9,8,7]