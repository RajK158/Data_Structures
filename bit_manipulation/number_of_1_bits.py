class Solution:

    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:
            n &= n - 1
            count += 1

        return count


if __name__ == "__main__":

    sol = Solution()

    print(sol.hammingWeight(23))          # 4
    print(sol.hammingWeight(2147483645))  # 30
    print(sol.hammingWeight(0))           # 0