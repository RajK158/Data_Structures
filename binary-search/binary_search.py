# Problem: Binary Search
# Pattern: Binary Search
# Time: O(log n)
# Space: O(1)

from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return -1


if __name__ == "__main__":

    sol = Solution()

    print(sol.search([-1,0,2,4,6,8], 4))  # 3
    print(sol.search([-1,0,2,4,6,8], 3))  # -1
    print(sol.search([1], 1))             # 0