# Problem: LRU Cache
# Pattern: HashMap + Doubly Linked List
# Time:
# get -> O(1)
# put -> O(1)
# Space: O(capacity)

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):

        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def get(self, key):

        if key in self.cache:

            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1

    def put(self, key, value):

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)

        self.insert(self.cache[key])

        if len(self.cache) > self.cap:

            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":

    cache = LRUCache(2)

    cache.put(1, 10)

    print(cache.get(1))  # 10

    cache.put(2, 20)
    cache.put(3, 30)

    print(cache.get(2))  # 20
    print(cache.get(1))  # -1