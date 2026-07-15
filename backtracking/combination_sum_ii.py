# Problem: Combination Sum II
# Pattern: Backtracking
# Time: O(2^n)
# Space: O(n)

from typing import List

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def dfs(start, cur, total):

            if total == target:
                res.append(cur.copy())
                return

            if total > target:
                return

            prev = -1

            for i in range(start, len(candidates)):

                if candidates[i] == prev:
                    continue

                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()

                prev = candidates[i]

        dfs(0, [], 0)

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.combinationSum2([9,2,2,4,6,1,5], 8))
    print(sol.combinationSum2([1,2,3,4,5], 7))