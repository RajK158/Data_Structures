# Problem: Remove Nth Node From End of List
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0, head)

        slow = dummy
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


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
                ListNode(4)
            )
        )
    )

    sol = Solution()

    new_head = sol.removeNthFromEnd(head, 2)

    print_list(new_head)