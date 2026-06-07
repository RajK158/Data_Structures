# Problem: Koko Eating Bananas
# Pattern: Binary Search on Answer
# Time: O(n log m), where m = max(piles)
# Space: O(1)

from typing import List
import math

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r

        while l <= r:

            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = k
                r = k - 1

            else:
                l = k + 1

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.minEatingSpeed([1,4,3,2], 9))      # 2
    print(sol.minEatingSpeed([25,10,23,4], 4))   # 25
    print(sol.minEatingSpeed([3,6,7,11], 8))     # 4