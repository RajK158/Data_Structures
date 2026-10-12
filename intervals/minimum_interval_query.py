from typing import List
import heapq


class Solution:

    def minInterval(
        self,
        intervals: List[List[int]],
        queries: List[int]
    ) -> List[int]:

        intervals.sort()
        sorted_queries = sorted(queries)

        min_heap = []
        res = {}
        i = 0

        for q in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= q:

                left, right = intervals[i]
                length = right - left + 1

                heapq.heappush(
                    min_heap,
                    (length, right)
                )

                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                res[q] = min_heap[0][0]
            else:
                res[q] = -1

        return [res[q] for q in queries]


if __name__ == "__main__":

    sol = Solution()

    print(sol.minInterval(
        [[1,3], [2,3], [3,7], [6,6]],
        [2,3,1,7,6,8]
    ))