from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        removals = 0
        end = intervals[0][1]

        for start, finish in intervals[1:]:

            if start < end:
                removals += 1

            else:
                end = finish

        return removals


if __name__ == "__main__":

    sol = Solution()

    print(sol.eraseOverlapIntervals(
        [[1,2], [2,4], [1,4]]
    ))  # 1

    print(sol.eraseOverlapIntervals(
        [[1,2], [2,4]]
    ))  # 0