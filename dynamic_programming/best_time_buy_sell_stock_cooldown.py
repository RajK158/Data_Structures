from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:

            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(
                prev_hold,
                prev_rest - price
            )

            sold = prev_hold + price

            rest = max(
                prev_rest,
                prev_sold
            )

        return max(sold, rest)


if __name__ == "__main__":

    sol = Solution()

    print(sol.maxProfit([1,3,4,0,4]))  # 6
    print(sol.maxProfit([1]))          # 0
    print(sol.maxProfit([1,2,3,0,2]))  # 3