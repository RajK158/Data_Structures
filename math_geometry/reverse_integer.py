class Solution:

    def reverse(self, x: int) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x:

            digit = x % 10
            x //= 10

            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        result *= sign

        if result < INT_MIN or result > INT_MAX:
            return 0

        return result


if __name__ == "__main__":

    sol = Solution()

    print(sol.reverse(1234))        # 4321
    print(sol.reverse(-1234))       # -4321
    print(sol.reverse(120))         # 21
    print(sol.reverse(1234236467))  # 0