# Problem: Daily Temperatures
# Pattern: Monotonic Stack
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):

            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev

            stack.append(i)

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.dailyTemperatures([30,38,30,36,35,40,28]))
    print(sol.dailyTemperatures([22,21,20]))
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))