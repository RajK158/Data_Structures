from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:

        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(
                farthest,
                i + nums[i]
            )

            if i == end:
                jumps += 1
                end = farthest

        return jumps


if __name__ == "__main__":

    sol = Solution()

    print(sol.jump([2,4,1,1,1,1]))  # 2
    print(sol.jump([2,1,2,1,0]))    # 2
    print(sol.jump([0]))             # 0