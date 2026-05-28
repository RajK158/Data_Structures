# Problem: Valid Parentheses
# Pattern: Stack
# Time: O(n)
# Space: O(n)

class Solution:

    def isValid(self, s: str) -> bool:

        stack = []

        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:

            if c in close_to_open:

                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)

        return len(stack) == 0


if __name__ == "__main__":

    sol = Solution()

    print(sol.isValid("[]"))        # True
    print(sol.isValid("([{}])"))    # True
    print(sol.isValid("[(])"))      # False
    print(sol.isValid("(()"))       # False