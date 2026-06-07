# Problem: Search in Rotated Sorted Array
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

            # Left half sorted
            if nums[l] <= nums[mid]:

                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Right half sorted
            else:

                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


if __name__ == "__main__":

    sol = Solution()

    print(sol.search([3,4,5,6,1,2], 1))  # 4
    print(sol.search([3,5,6,0,1,2], 4))  # -1
    print(sol.search([4,5,6,7,0,1,2], 0)) # 4