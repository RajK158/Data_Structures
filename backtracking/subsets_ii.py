from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, subset):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.subsetsWithDup([1, 2, 1]))
    print(sol.subsetsWithDup([7, 7]))