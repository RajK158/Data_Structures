# Problem: Design Add and Search Word Data Structure
# Pattern: Trie + DFS
# Add: O(n)
# Search: O(n) average, O(26^d * n) with d wildcards
# Space: O(total characters inserted)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):

        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]

        cur.end = True

    def search(self, word):

        def dfs(node, i):

            if i == len(word):
                return node.end

            ch = word[i]

            if ch == ".":

                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True

                return False

            if ch not in node.children:
                return False

            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)


if __name__ == "__main__":

    wd = WordDictionary()

    wd.addWord("day")
    wd.addWord("bay")
    wd.addWord("may")

    print(wd.search("say"))
    print(wd.search("day"))
    print(wd.search(".ay"))
    print(wd.search("b.."))