# Problem: Find the Duplicate Number
# Pattern: Floyd's Cycle Detection
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


if __name__ == "__main__":

    sol = Solution()

    print(sol.findDuplicate([1,2,3,2,2]))  # 2
    print(sol.findDuplicate([1,2,3,4,4]))  # 4
    print(sol.findDuplicate([3,1,3,4,2]))  # 3