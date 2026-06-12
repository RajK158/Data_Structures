# Problem: Merge Two Sorted Linked Lists
# Pattern: Linked List
# Time: O(n + m)
# Space: O(1)

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next


def print_list(head):

    while head:
        print(head.val, end=" ")
        head = head.next

    print()


if __name__ == "__main__":

    list1 = ListNode(
        1,
        ListNode(
            2,
            ListNode(4)
        )
    )

    list2 = ListNode(
        1,
        ListNode(
            3,
            ListNode(5)
        )
    )

    sol = Solution()

    merged = sol.mergeTwoLists(list1, list2)

    print_list(merged)