# Problem: Car Fleet
# Pattern: Stack / Sorting
# Time: O(n log n)
# Space: O(n)

from typing import List

class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time = 0

        for p, s in cars:

            time = (target - p) / s

            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets


if __name__ == "__main__":

    sol = Solution()

    print(sol.carFleet(10, [1,4], [3,2]))          # 1
    print(sol.carFleet(10, [4,1,0,7], [2,2,1,1])) # 3
    print(sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3