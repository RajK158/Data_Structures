from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            for c in range(left, right + 1):
                res.append(matrix[top][c])

            top += 1

            for r in range(top, bottom + 1):
                res.append(matrix[r][right])

            right -= 1

            if top <= bottom:

                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])

                bottom -= 1

            if left <= right:

                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])

                left += 1

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.spiralOrder([
        [1,2],
        [3,4]
    ]))

    print(sol.spiralOrder([
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]))

    print(sol.spiralOrder([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]))