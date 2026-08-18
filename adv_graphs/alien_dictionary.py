from typing import List
from collections import defaultdict, deque


class Solution:

    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for ch in word:
                indegree[ch] = 0

        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1]

            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):

                if w1[j] != w2[j]:

                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1

                    break

        q = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        res = []

        while q:

            ch = q.popleft()
            res.append(ch)

            for nei in graph[ch]:

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(indegree):
            return ""

        return "".join(res)


if __name__ == "__main__":

    sol = Solution()

    print(sol.foreignDictionary(["z", "o"]))
    print(sol.foreignDictionary(["hrn", "hrf", "er", "enn", "rfnn"]))
    print(sol.foreignDictionary(["abc", "ab"]))