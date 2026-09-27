from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):

            if i + nums[i] >= goal:
                goal = i

        return goal == 0


if __name__ == "__main__":

    sol = Solution()

    print(sol.canJump([1,2,0,1,0]))  # True
    print(sol.canJump([1,2,1,0,1]))  # False
    print(sol.canJump([0]))           # True