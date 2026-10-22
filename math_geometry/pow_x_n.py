class Solution:

    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:

            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result


if __name__ == "__main__":

    sol = Solution()

    print(sol.myPow(2.0, 5))    # 32.0
    print(sol.myPow(1.1, 10))   # 2.593742...
    print(sol.myPow(2.0, -3))   # 0.125