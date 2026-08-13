from typing import List
from collections import defaultdict
import heapq


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):

            while graph[airport]:
                nxt = heapq.heappop(graph[airport])
                dfs(nxt)

            route.append(airport)

        dfs("JFK")

        return route[::-1]


if __name__ == "__main__":

    sol = Solution()

    print(sol.findItinerary([
        ["BUF", "HOU"],
        ["HOU", "SEA"],
        ["JFK", "BUF"]
    ]))

    print(sol.findItinerary([
        ["HOU", "JFK"],
        ["SEA", "JFK"],
        ["JFK", "SEA"],
        ["JFK", "HOU"]
    ]))