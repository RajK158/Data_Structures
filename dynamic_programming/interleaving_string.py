class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        rows = len(s1)
        cols = len(s2)

        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols] = True

        for i in range(rows, -1, -1):

            for j in range(cols, -1, -1):

                if i == rows and j == cols:
                    continue

                if (
                    i < rows
                    and s1[i] == s3[i + j]
                    and dp[i + 1][j]
                ):
                    dp[i][j] = True

                if (
                    j < cols
                    and s2[j] == s3[i + j]
                    and dp[i][j + 1]
                ):
                    dp[i][j] = True

        return dp[0][0]


if __name__ == "__main__":

    sol = Solution()

    print(sol.isInterleave(
        "aaaa",
        "bbbb",
        "aabbbbaa"
    ))  # True

    print(sol.isInterleave(
        "",
        "",
        ""
    ))  # True

    print(sol.isInterleave(
        "abc",
        "xyz",
        "abxzcy"
    ))  # False