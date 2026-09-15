from typing import List


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {0: 1}

        for num in nums:

            next_dp = {}

            for total, count in dp.items():

                next_dp[total + num] = (
                    next_dp.get(total + num, 0) + count
                )

                next_dp[total - num] = (
                    next_dp.get(total - num, 0) + count
                )

            dp = next_dp

        return dp.get(target, 0)


if __name__ == "__main__":

    sol = Solution()

    print(sol.findTargetSumWays([2,2,2], 2))       # 3
    print(sol.findTargetSumWays([1,1], 0))         # 2
    print(sol.findTargetSumWays([1], 1))           # 1
    print(sol.findTargetSumWays([1], 2))           # 0