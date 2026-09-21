from typing import List


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        def dfs(r, c):

            if dp[r][c] != 0:
                return dp[r][c]

            best = 1

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]
                ):

                    best = max(
                        best,
                        1 + dfs(nr, nc)
                    )

            dp[r][c] = best

            return best

        res = 0

        for r in range(rows):
            for c in range(cols):
                res = max(
                    res,
                    dfs(r, c)
                )

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.longestIncreasingPath([
        [5,5,3],
        [2,3,6],
        [1,1,1]
    ]))  # 4

    print(sol.longestIncreasingPath([
        [1,2,3],
        [2,1,4],
        [7,6,5]
    ]))  # 7