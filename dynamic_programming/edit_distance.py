class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i

        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):

            for j in range(n - 1, -1, -1):

                if word1[i] == word2[j]:

                    dp[i][j] = dp[i + 1][j + 1]

                else:

                    dp[i][j] = 1 + min(
                        dp[i][j + 1],
                        dp[i + 1][j],
                        dp[i + 1][j + 1]
                    )

        return dp[0][0]


if __name__ == "__main__":

    sol = Solution()

    print(sol.minDistance("monkeys", "money"))      # 2
    print(sol.minDistance("neatcdee", "neetcode"))  # 3
    print(sol.minDistance("", "abc"))               # 3