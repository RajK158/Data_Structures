from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:

        rob1 = 0
        rob2 = 0

        for n in nums:

            current = max(
                rob2,
                rob1 + n
            )

            rob1 = rob2
            rob2 = current

        return rob2


if __name__ == "__main__":

    sol = Solution()

    print(sol.rob([1,1,3,3]))      # 4
    print(sol.rob([2,9,8,3,6]))    # 16
    print(sol.rob([2,7,9,3,1]))    # 12