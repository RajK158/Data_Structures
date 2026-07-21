from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                if not is_palindrome(start, end):
                    continue

                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.partition("aab"))
    print(sol.partition("a"))
    print(sol.partition("abba"))