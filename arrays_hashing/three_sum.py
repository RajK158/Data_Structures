# Problem: 3Sum
# Pattern: Sorting + Two Pointers
# Time: O(n^2)
# Space: O(1) extra, excluding output

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([0,0,0]))
    print(sol.threeSum([1,2,-2,-1]))