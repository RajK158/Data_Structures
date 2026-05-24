# Problem: Longest Substring Without Repeating Characters
# Pattern: Sliding Window
# Time: O(n)
# Space: O(n)

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l = 0
        longest = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest


if __name__ == "__main__":

    sol = Solution()

    print(sol.lengthOfLongestSubstring("zxyzxyz"))  # 3
    print(sol.lengthOfLongestSubstring("xxxx"))     # 1
    print(sol.lengthOfLongestSubstring(""))         # 0