# Problem: Two Integer Sum II
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:

            cur_sum = numbers[l] + numbers[r]

            if cur_sum > target:
                r -= 1

            elif cur_sum < target:
                l += 1

            else:
                return [l + 1, r + 1]


if __name__ == "__main__":

    sol = Solution()

    print(sol.twoSum([1,2,3,4], 3))      # [1,2]
    print(sol.twoSum([2,7,11,15], 9))    # [1,2]
    print(sol.twoSum([-1,0], -1))        # [1,2]