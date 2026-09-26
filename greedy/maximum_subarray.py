from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        cur_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:

            cur_sum = max(
                num,
                cur_sum + num
            )

            max_sum = max(
                max_sum,
                cur_sum
            )

        return max_sum


if __name__ == "__main__":

    sol = Solution()

    print(sol.maxSubArray([2,-3,4,-2,2,1,-1,4]))  # 8
    print(sol.maxSubArray([-1]))                    # -1
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6