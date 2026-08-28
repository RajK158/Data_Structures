class Solution:

    def countSubstrings(self, s: str) -> int:

        res = 0

        for i in range(len(s)):

            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.countSubstrings("abc"))  # 3
    print(sol.countSubstrings("aaa"))  # 6
    print(sol.countSubstrings("aba"))  # 4