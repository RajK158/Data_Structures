class Solution:

    def getSum(self, a: int, b: int) -> int:

        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:

            carry = (a & b) << 1

            a = (a ^ b) & MASK
            b = carry & MASK

        if a <= MAX_INT:
            return a

        return ~(a ^ MASK)


if __name__ == "__main__":

    sol = Solution()

    print(sol.getSum(1, 1))     # 2
    print(sol.getSum(4, 7))     # 11
    print(sol.getSum(-3, 5))    # 2
    print(sol.getSum(-4, -6))   # -10