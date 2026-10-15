from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False

        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True

        for r in range(1, rows):

            for c in range(cols):

                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):

            for c in range(1, cols):

                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:

            for r in range(rows):
                matrix[r][0] = 0

        if first_row_zero:

            for c in range(cols):
                matrix[0][c] = 0


if __name__ == "__main__":

    sol = Solution()

    matrix1 = [
        [0,1],
        [1,0]
    ]

    sol.setZeroes(matrix1)
    print(matrix1)

    matrix2 = [
        [1,2,3],
        [4,0,5],
        [6,7,8]
    ]

    sol.setZeroes(matrix2)
    print(matrix2)