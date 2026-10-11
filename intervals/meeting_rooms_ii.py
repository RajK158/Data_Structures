import heapq


class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:

    def minMeetingRooms(self, intervals):

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        min_heap = []

        for interval in intervals:

            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            heapq.heappush(
                min_heap,
                interval.end
            )

        return len(min_heap)


if __name__ == "__main__":

    sol = Solution()

    intervals1 = [
        Interval(0, 40),
        Interval(5, 10),
        Interval(15, 20)
    ]

    intervals2 = [
        Interval(4, 9)
    ]

    intervals3 = [
        Interval(0, 8),
        Interval(8, 10)
    ]

    print(sol.minMeetingRooms(intervals1))  # 2
    print(sol.minMeetingRooms(intervals2))  # 1
    print(sol.minMeetingRooms(intervals3))  # 1