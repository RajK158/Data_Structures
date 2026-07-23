# Problem: Implement Trie (Prefix Tree)
# Pattern: Trie
# Time:
# insert  : O(n)
# search  : O(n)
# startsWith : O(n)
# Space: O(total characters inserted)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            cur = cur.children[ch]

        cur.end = True

    def search(self, word):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                return False

            cur = cur.children[ch]

        return cur.end

    def startsWith(self, prefix):
        cur = self.root

        for ch in prefix:
            if ch not in cur.children:
                return False

            cur = cur.children[ch]

        return True


if __name__ == "__main__":

    trie = Trie()

    trie.insert("dog")

    print(trie.search("dog"))
    print(trie.search("do"))
    print(trie.startsWith("do"))

    trie.insert("do")

    print(trie.search("do"))