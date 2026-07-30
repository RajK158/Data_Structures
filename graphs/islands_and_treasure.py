# Problem: Islands and Treasure
# Pattern: Multi-Source BFS
# Time: O(m * n)
# Space: O(m * n)

from collections import deque
from typing import List


class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:

            r, c = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    grid[nr][nc] != 2147483647
                ):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))


if __name__ == "__main__":

    INF = 2147483647

    grid = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]
    ]

    sol = Solution()
    sol.islandsAndTreasure(grid)

    for row in grid:
        print(row)