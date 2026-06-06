# Problem: Find Minimum in Rotated Sorted Array
# Pattern: Binary Search
# Time: O(log n)
# Space: O(1)

from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]


if __name__ == "__main__":

    sol = Solution()

    print(sol.findMin([3,4,5,6,1,2]))  # 1
    print(sol.findMin([4,5,0,1,2,3]))  # 0
    print(sol.findMin([4,5,6,7]))      # 4