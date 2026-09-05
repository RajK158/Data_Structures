from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}

        for n in nums:

            next_dp = dp.copy()

            for s in dp:
                next_dp.add(s + n)

            dp = next_dp

            if target in dp:
                return True

        return False


if __name__ == "__main__":

    sol = Solution()

    print(sol.canPartition([1,2,3,4]))    # True
    print(sol.canPartition([1,2,3,4,5]))  # False
    print(sol.canPartition([1,5,11,5]))   # True