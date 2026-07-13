# Problem: Subsets
# Pattern: Backtracking
# Time: O(n * 2^n)
# Space: O(n)

from typing import List

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i):

            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.subsets([1,2,3]))
    print(sol.subsets([7]))