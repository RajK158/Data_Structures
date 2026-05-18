# Problem: Product of Array Except Self
# Pattern: Prefix & Postfix Products
# Time: O(n)
# Space: O(1) extra

from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# 🔥 Driver code
if __name__ == "__main__":

    sol = Solution()

    print(sol.productExceptSelf([1,2,4,6]))      # [48,24,12,8]
    print(sol.productExceptSelf([-1,0,1,2,3]))   # [0,-6,0,0,0]# Problem: Product of Array Except Self
# Pattern: Prefix & Postfix Products
# Time: O(n)
# Space: O(1) extra

from typing import List

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


