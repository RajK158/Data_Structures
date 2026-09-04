from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):

            for j in range(i + 1, len(nums)):

                if nums[i] < nums[j]:

                    dp[i] = max(
                        dp[i],
                        1 + dp[j]
                    )

        return max(dp)


if __name__ == "__main__":

    sol = Solution()

    print(sol.lengthOfLIS([9,1,4,2,3,3,7]))  # 4
    print(sol.lengthOfLIS([0,3,1,3,2,3]))    # 4
    print(sol.lengthOfLIS([7,7,7]))          # 1