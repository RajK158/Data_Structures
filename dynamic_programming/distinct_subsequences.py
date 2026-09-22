class Solution:

    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):

            for j in range(n - 1, -1, -1):

                dp[i][j] = dp[i + 1][j]

                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]


if __name__ == "__main__":

    sol = Solution()

    print(sol.numDistinct("caaat", "cat"))  # 3
    print(sol.numDistinct("xxyxy", "xy"))   # 5
    print(sol.numDistinct("abc", "abc"))    # 1
    print(sol.numDistinct("abc", "abcd"))   # 0