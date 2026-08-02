class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # head's previous is None
        curr = head

        while curr:
            next_node = curr.next  # save not to lose reference to next node
            curr.next = prev  # reverse current's next 
            prev = curr  # new previous is current
            curr = next_node  # new current is the original next
            
        return prev