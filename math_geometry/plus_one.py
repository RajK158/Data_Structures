from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


if __name__ == "__main__":

    sol = Solution()

    print(sol.plusOne([1,2,3,4]))  # [1,2,3,5]
    print(sol.plusOne([9,9,9]))    # [1,0,0,0]
    print(sol.plusOne([4,9,9]))    # [5,0,0]