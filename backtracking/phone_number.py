# Problem: Letter Combinations of a Phone Number
# Pattern: Backtracking
# Time: O(4^n * n)
# Space: O(n)

from typing import List

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []

        def backtrack(i):

            if i == len(digits):
                res.append("".join(path))
                return

            for ch in phone[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.letterCombinations("23"))
    print(sol.letterCombinations("2"))# Problem: Letter Combinations of a Phone Number
# Pattern: Backtracking
# Time: O(4^n * n)
# Space: O(n)

from typing import List

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []

        def backtrack(i):

            if i == len(digits):
                res.append("".join(path))
                return

            for ch in phone[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.letterCombinations("23"))
    print(sol.letterCombinations("2"))