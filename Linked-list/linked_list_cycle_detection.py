# Problem: Linked List Cycle Detection
# Pattern: Fast & Slow Pointers
# Time: O(n)
# Space: O(1)

class ListNode:

    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:

    def hasCycle(self, head) -> bool:

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == "__main__":

    # 1 -> 2 -> 3 -> 4
    #      ^         |
    #      |_________|

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2

    sol = Solution()

    print(sol.hasCycle(n1))  # True

    a = ListNode(1)
    b = ListNode(2)

    a.next = b

    print(sol.hasCycle(a))   # False