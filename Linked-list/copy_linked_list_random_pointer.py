# Problem: Copy Linked List with Random Pointer
# Pattern: HashMap + Linked List
# Time: O(n)
# Space: O(n)

class Node:

    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head):

        old_to_copy = {None: None}

        curr = head

        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]


def print_list(head):

    nodes = []
    curr = head

    while curr:
        random_val = curr.random.val if curr.random else None
        nodes.append([curr.val, random_val])
        curr = curr.next

    print(nodes)


if __name__ == "__main__":

    n1 = Node(3)
    n2 = Node(7)
    n3 = Node(4)
    n4 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    n1.random = None
    n2.random = n4
    n3.random = n1
    n4.random = n2

    sol = Solution()

    copied = sol.copyRandomList(n1)

    print_list(copied)