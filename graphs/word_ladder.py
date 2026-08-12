from typing import List
from collections import deque


class Solution:

    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:

            word, length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word, length + 1))

        return 0


if __name__ == "__main__":

    sol = Solution()

    print(sol.ladderLength(
        "cat",
        "sag",
        ["bat", "bag", "sag", "dag", "dot"]
    ))  # 4

    print(sol.ladderLength(
        "cat",
        "sag",
        ["bat", "bag", "sat", "dag", "dot"]
    ))  # 0