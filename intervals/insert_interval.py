from typing import List


class Solution:

    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:

        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:

            newInterval[0] = min(
                newInterval[0],
                intervals[i][0]
            )

            newInterval[1] = max(
                newInterval[1],
                intervals[i][1]
            )

            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.insert(
        [[1,3], [4,6]],
        [2,5]
    ))  # [[1,6]]

    print(sol.insert(
        [[1,2], [3,5], [9,10]],
        [6,7]
    ))  # [[1,2], [3,5], [6,7], [9,10]]