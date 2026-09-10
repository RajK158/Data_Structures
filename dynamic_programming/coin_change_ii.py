from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:

            for a in range(coin, amount + 1):

                dp[a] += dp[a - coin]

        return dp[amount]


if __name__ == "__main__":

    sol = Solution()

    print(sol.change(4, [1,2,3]))  # 4
    print(sol.change(7, [2,4]))    # 0
    print(sol.change(0, [1,2,5]))  # 1