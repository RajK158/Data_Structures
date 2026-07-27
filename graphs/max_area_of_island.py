# Problem: Max Area of Island
# Pattern: Graph / DFS
# Time: O(m * n)
# Space: O(m * n) (worst-case recursion stack)

from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        def dfs(r, c):

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0

            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))

        return ans


if __name__ == "__main__":

    sol = Solution()

    grid = [
        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]
    ]

    print(sol.maxAreaOfIsland(grid))