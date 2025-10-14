class LLCycle:

    def __init__(self):
        pass

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while slow and fast.next:

            slow = slow.next 
            fast = fast.next.next

            if slow == fast:
                return True
        return False