from typing import List
import heapq


class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)

        min_heap = [(grid[0][0], 0, 0)]
        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while min_heap:

            time, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nr >= n
                    or nc < 0 or nc >= n
                    or (nr, nc) in visited
                ):
                    continue

                new_time = max(
                    time,
                    grid[nr][nc]
                )

                heapq.heappush(
                    min_heap,
                    (new_time, nr, nc)
                )


if __name__ == "__main__":

    sol = Solution()

    print(sol.swimInWater([
        [0,1],
        [2,3]
    ]))  # 3

    print(sol.swimInWater([
        [0,1,2,10],
        [9,14,4,13],
        [12,3,8,15],
        [11,5,7,6]
    ]))  # 8