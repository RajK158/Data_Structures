from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for num in nums:
            result ^= num

        return result


if __name__ == "__main__":

    sol = Solution()

    print(sol.singleNumber([3,2,3]))        # 2
    print(sol.singleNumber([7,6,6,7,8]))    # 8
    print(sol.singleNumber([5]))            # 5