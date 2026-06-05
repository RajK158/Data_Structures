# Problem: Search a 2D Matrix
# Pattern: Binary Search
# Time: O(log(m * n))
# Space: O(1)

from typing import List

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:

            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False


if __name__ == "__main__":

    sol = Solution()

    matrix = [
        [1,2,4,8],
        [10,11,12,13],
        [14,20,30,40]
    ]

    print(sol.searchMatrix(matrix, 10))  # True
    print(sol.searchMatrix(matrix, 15))  # False