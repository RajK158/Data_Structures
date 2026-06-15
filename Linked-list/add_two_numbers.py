# Problem: Add Two Numbers
# Pattern: Linked List
# Time: O(max(n, m))
# Space: O(max(n, m))

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry

            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)

            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()


if __name__ == "__main__":

    l1 = ListNode(
        1,
        ListNode(
            2,
            ListNode(3)
        )
    )

    l2 = ListNode(
        4,
        ListNode(
            5,
            ListNode(6)
        )
    )

    sol = Solution()

    result = sol.addTwoNumbers(l1, l2)

    print_list(result)