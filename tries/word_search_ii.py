# Problem: Word Search II
# Pattern: Trie + Backtracking
# Time: O(M*N*4^L)
# Space: O(total characters in Trie)

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.word = word

        rows = len(board)
        cols = len(board[0])

        ans = []

        def dfs(r, c, node):

            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
            ):
                return

            ch = board[r][c]

            if ch == "#" or ch not in node.children:
                return

            nxt = node.children[ch]

            if nxt.word:
                ans.append(nxt.word)
                nxt.word = None

            board[r][c] = "#"

            dfs(r + 1, c, nxt)
            dfs(r - 1, c, nxt)
            dfs(r, c + 1, nxt)
            dfs(r, c - 1, nxt)

            board[r][c] = ch

            if not nxt.children:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return ans


if __name__ == "__main__":

    sol = Solution()

    board = [
        ["a","b","c","d"],
        ["s","a","a","t"],
        ["a","c","k","e"],
        ["a","c","d","n"]
    ]

    words = ["bat","cat","back","backend","stack"]

    print(sol.findWords(board, words))

    board2 = [
        ["x","o"],
        ["x","o"]
    ]

    print(sol.findWords(board2, ["xoxo"]))