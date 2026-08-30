from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):

            for coin in coins:

                if coin <= a:
                    dp[a] = min(
                        dp[a],
                        1 + dp[a - coin]
                    )

        if dp[amount] == amount + 1:
            return -1

        return dp[amount]


if __name__ == "__main__":

    sol = Solution()

    print(sol.coinChange([1,5,10], 12))  # 3
    print(sol.coinChange([2], 3))        # -1
    print(sol.coinChange([1], 0))        # 0