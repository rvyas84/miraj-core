from typing import Optional


class LLCycle:
    """
    A class to detect if a linked list has a cycle.

    Methods
    -------
    hasCycle(head: ListNode) -> bool:
        Determines if the linked list has a cycle using the Floyd's Tortoise and Hare algorithm.
    """

    def __init__(self):
        pass

    def hasCycle(self, head) -> bool:
        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            if slow == fast:
                return True
        return False