# Problem: Number of Islands
# Pattern: Graph / DFS
# Time: O(m * n)
# Space: O(m * n) (worst-case recursion stack)

from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands


if __name__ == "__main__":

    sol = Solution()

    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    print(sol.numIslands(grid1))
    print(sol.numIslands(grid2))