from typing import List
from collections import deque


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:

            for _ in range(len(q)):

                r, c = q.popleft()

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0 or nr >= rows
                        or nc < 0 or nc >= cols
                        or grid[nr][nc] != 1
                    ):
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1


if __name__ == "__main__":

    sol = Solution()

    print(sol.orangesRotting([
        [1, 1, 0],
        [0, 1, 1],
        [0, 1, 2]
    ]))  # 4

    print(sol.orangesRotting([
        [1, 0, 1],
        [0, 2, 0],
        [1, 0, 1]
    ]))  # -1

    print(sol.orangesRotting([
        [0, 2]
    ]))  # 0