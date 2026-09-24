from typing import List


class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):

            for left in range(1, n - length):

                right = left + length - 1

                for i in range(left, right + 1):

                    coins = (
                        nums[left - 1] * nums[i] * nums[right + 1]
                        + dp[left][i - 1]
                        + dp[i + 1][right]
                    )

                    dp[left][right] = max(
                        dp[left][right],
                        coins
                    )

        return dp[1][n - 2]


if __name__ == "__main__":

    sol = Solution()

    print(sol.maxCoins([4,2,3,7]))  # 143
    print(sol.maxCoins([3,1,5,8]))  # 167
    print(sol.maxCoins([1]))        # 1