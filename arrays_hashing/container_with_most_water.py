# Problem: Container With Most Water
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            max_water = max(max_water, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water


if __name__ == "__main__":
    sol = Solution()

    print(sol.maxArea([1,7,2,5,4,7,3,6]))  # 36
    print(sol.maxArea([2,2,2]))             # 4