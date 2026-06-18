# Problem: Merge K Sorted Linked Lists
# Pattern: Heap / Priority Queue
# Time: O(n log k)
# Space: O(k)

from typing import List
import heapq

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List):

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()


if __name__ == "__main__":

    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(5)))
    l3 = ListNode(3, ListNode(6))

    sol = Solution()

    merged = sol.mergeKLists([l1, l2, l3])

    print_list(merged)