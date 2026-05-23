# Problem: Best Time to Buy and Sell Stock
# Pattern: Sliding Window / Two Pointers
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            else:
                l = r

            r += 1

        return max_profit


if __name__ == "__main__":

    sol = Solution()

    print(sol.maxProfit([10,1,5,6,7,1]))  # 6
    print(sol.maxProfit([10,8,7,5,2]))    # 0
    print(sol.maxProfit([7,1,5,3,6,4]))   # 5