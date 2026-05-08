# Problem: Valid Anagram
# Pattern: Frequency Count
# Time: O(n)
# Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return False

        return True


# 🔥 Driver code (this is what you were missing)
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False