# Problem: Median of Two Sorted Arrays
# Pattern: Binary Search Partition
# Time: O(log(min(m, n)))
# Space: O(1)

from typing import List

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:

            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")

            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1

            else:
                l = i + 1


if __name__ == "__main__":

    sol = Solution()

    print(sol.findMedianSortedArrays([1,2], [3]))      # 2.0
    print(sol.findMedianSortedArrays([1,3], [2,4]))    # 2.5
    print(sol.findMedianSortedArrays([], [1]))         # 1.0