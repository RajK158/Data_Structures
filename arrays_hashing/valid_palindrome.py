# Problem: Valid Palindrome
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)

class Solution:

    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


if __name__ == "__main__":

    sol = Solution()

    print(sol.isPalindrome("Was it a car or a cat I saw?"))  # True
    print(sol.isPalindrome("tab a cat"))                     # False
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True