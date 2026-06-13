# Problem: Reorder Linked List
# Pattern: Linked List
# Time: O(n)
# Space: O(1)

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first = head
        second = prev

        while second:

            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()


if __name__ == "__main__":

    head = ListNode(
        2,
        ListNode(
            4,
            ListNode(
                6,
                ListNode(
                    8,
                    ListNode(10)
                )
            )
        )
    )

    sol = Solution()

    sol.reorderList(head)

    print_list(head)