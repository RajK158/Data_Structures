from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):

            rob1 = 0
            rob2 = 0

            for n in houses:

                current = max(
                    rob2,
                    rob1 + n
                )

                rob1 = rob2
                rob2 = current

            return rob2

        return max(
            rob_line(nums[:-1]),
            rob_line(nums[1:])
        )


if __name__ == "__main__":

    sol = Solution()

    print(sol.rob([3,4,3]))       # 4
    print(sol.rob([2,9,8,3,6]))   # 15
    print(sol.rob([1]))           # 1