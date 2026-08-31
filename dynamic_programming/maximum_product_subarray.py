from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for n in nums[1:]:

            temp = cur_max

            cur_max = max(
                n,
                n * cur_max,
                n * cur_min
            )

            cur_min = min(
                n,
                n * temp,
                n * cur_min
            )

            res = max(res, cur_max)

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.maxProduct([2,4,-3,5]))   # 8
    print(sol.maxProduct([-3,0,-2]))    # 0
    print(sol.maxProduct([2,3,-2,4]))   # 6
    print(sol.maxProduct([-2,3,-4]))    # 24