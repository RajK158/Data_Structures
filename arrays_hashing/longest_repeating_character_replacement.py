# Problem: Longest Repeating Character Replacement
# Pattern: Sliding Window
# Time: O(n)
# Space: O(1)

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.characterReplacement("XYYX", 2))     # 4
    print(sol.characterReplacement("AAABABB", 1))  # 5
    print(sol.characterReplacement("ABAB", 2))     # 4