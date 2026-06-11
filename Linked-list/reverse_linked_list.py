# Problem: Reverse Linked List
# Pattern: Linked List
# Time: O(n)
# Space: O(1)

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head):

        prev = None
        curr = head

        while curr:

            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        return prev


def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()


if __name__ == "__main__":

    head = ListNode(
        0,
        ListNode(
            1,
            ListNode(
                2,
                ListNode(3)
            )
        )
    )

    sol = Solution()

    new_head = sol.reverseList(head)

    print_list(new_head)