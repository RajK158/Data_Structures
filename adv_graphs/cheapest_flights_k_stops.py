from typing import List


class Solution:

    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):

            temp = prices.copy()

            for u, v, price in flights:

                if prices[u] == float("inf"):
                    continue

                temp[v] = min(
                    temp[v],
                    prices[u] + price
                )

            prices = temp

        if prices[dst] == float("inf"):
            return -1

        return prices[dst]


if __name__ == "__main__":

    sol = Solution()

    print(sol.findCheapestPrice(
        4,
        [
            [0,1,200],
            [1,2,100],
            [1,3,300],
            [2,3,100]
        ],
        0,
        3,
        1
    ))  # 500

    print(sol.findCheapestPrice(
        3,
        [
            [1,0,100],
            [1,2,200],
            [0,2,100]
        ],
        1,
        2,
        1
    ))  # 200