from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        result = len(nums)

        for i, num in enumerate(nums):
            result ^= i
            result ^= num

        return result


if __name__ == "__main__":

    sol = Solution()

    print(sol.missingNumber([1,2,3]))  # 0
    print(sol.missingNumber([0,2]))    # 1
    print(sol.missingNumber([3,0,1]))  # 2