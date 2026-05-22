# Problem: Trapping Rain Water
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        water = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                water += right_max - height[r]

        return water


if __name__ == "__main__":
    sol = Solution()

    print(sol.trap([0,2,0,3,1,0,1,3,2,1]))  # 9
    print(sol.trap([4,2,0,3,2,5]))           # 9
    print(sol.trap([1,2,3]))                 # 0