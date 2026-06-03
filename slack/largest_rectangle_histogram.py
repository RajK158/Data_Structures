# Problem: Largest Rectangle in Histogram
# Pattern: Monotonic Stack
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i, h in enumerate(heights):

            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h))

        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area


if __name__ == "__main__":

    sol = Solution()

    print(sol.largestRectangleArea([7,1,7,2,2,4]))  # 8
    print(sol.largestRectangleArea([1,3,7]))        # 7
    print(sol.largestRectangleArea([2,1,5,6,2,3]))  # 10