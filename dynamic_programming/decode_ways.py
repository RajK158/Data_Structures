class Solution:

    def numDecodings(self, s: str) -> int:

        one = 1
        two = 0

        for i in range(len(s) - 1, -1, -1):

            current = 0

            if s[i] != "0":

                current = one

                if (
                    i + 1 < len(s)
                    and 10 <= int(s[i:i + 2]) <= 26
                ):
                    current += two

            two = one
            one = current

        return one


if __name__ == "__main__":

    sol = Solution()

    print(sol.numDecodings("12"))    # 2
    print(sol.numDecodings("01"))    # 0
    print(sol.numDecodings("1012"))  # 2
    print(sol.numDecodings("226"))   # 3