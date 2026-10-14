from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        for r in range(n):

            for c in range(r + 1, n):

                matrix[r][c], matrix[c][r] = (
                    matrix[c][r],
                    matrix[r][c]
                )

        for row in matrix:
            row.reverse()


if __name__ == "__main__":

    sol = Solution()

    matrix1 = [
        [1,2],
        [3,4]
    ]

    sol.rotate(matrix1)
    print(matrix1)

    matrix2 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    sol.rotate(matrix2)
    print(matrix2)