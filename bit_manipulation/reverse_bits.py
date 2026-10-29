class Solution:

    def reverseBits(self, n: int) -> int:

        res = 0

        for _ in range(32):

            bit = n & 1

            res = (res << 1) | bit

            n >>= 1

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.reverseBits(21))  # 2818572288