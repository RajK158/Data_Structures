from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):

            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start


if __name__ == "__main__":

    sol = Solution()

    print(sol.canCompleteCircuit(
        [1,2,3,4,5],
        [3,4,5,1,2]
    ))  # 3

    print(sol.canCompleteCircuit(
        [2,3,4],
        [3,4,3]
    ))  # -1