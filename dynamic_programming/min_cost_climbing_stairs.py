from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        one = 0
        two = 0

        for i in range(len(cost) - 1, -1, -1):

            current = cost[i] + min(one, two)

            two = one
            one = current

        return min(one, two)


if __name__ == "__main__":

    sol = Solution()

    print(sol.minCostClimbingStairs([1,2,3]))              # 2
    print(sol.minCostClimbingStairs([1,2,1,2,1,1,1]))      # 4
    print(sol.minCostClimbingStairs([10,15,20]))            # 15