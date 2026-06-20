# Problem: Reverse Nodes in K-Group
# Pattern: Linked List
# Time: O(n)
# Space: O(1)

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head, k):

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:

            kth = group_prev

            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            group_next = kth.next

            prev = group_next
            curr = group_prev.next

            while curr != group_next:

                nxt = curr.next
                curr.next = prev

                prev = curr
                curr = nxt

            tmp = group_prev.next

            group_prev.next = kth
            group_prev = tmp


def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()


if __name__ == "__main__":

    head = ListNode(
        1,
        ListNode(
            2,
            ListNode(
                3,
                ListNode(
                    4,
                    ListNode(
                        5,
                        ListNode(6)
                    )
                )
            )
        )
    )

    sol = Solution()

    result = sol.reverseKGroup(head, 3)

    print_list(result)