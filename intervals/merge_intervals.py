from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:

            last_end = res[-1][1]

            if start <= last_end:

                res[-1][1] = max(
                    last_end,
                    end
                )

            else:
                res.append([start, end])

        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.merge(
        [[1,3], [1,5], [6,7]]
    ))  # [[1,5], [6,7]]

    print(sol.merge(
        [[1,2], [2,3]]
    ))  # [[1,3]]