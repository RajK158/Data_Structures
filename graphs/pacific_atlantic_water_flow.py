from typing import List


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, previous_height):

            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or (r, c) in visited
                or heights[r][c] < previous_height
            ):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res


if __name__ == "__main__":

    sol = Solution()

    heights1 = [
        [4, 2, 7, 3, 4],
        [7, 4, 6, 4, 7],
        [6, 3, 5, 3, 6]
    ]

    heights2 = [
        [1],
        [1]
    ]

    print(sol.pacificAtlantic(heights1))
    print(sol.pacificAtlantic(heights2))