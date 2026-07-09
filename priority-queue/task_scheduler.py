# Problem: Task Scheduler
# Pattern: Heap + Queue
# Time: O(n log 26)
# Space: O(26)

from typing import List
from collections import Counter, deque
import heapq

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time


if __name__ == "__main__":

    sol = Solution()

    print(sol.leastInterval(["X","X","Y","Y"], 2))          # 5
    print(sol.leastInterval(["A","A","A","B","C"], 3))      # 9
    print(sol.leastInterval(["A","A","A","B","B","B"], 2))  # 8