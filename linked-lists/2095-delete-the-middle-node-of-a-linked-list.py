# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # head can change, use a dummy node
        prev, slow, fast = dummy, head, head  # previous of middle node, middle node, end of list

        while fast and fast.next:
            fast = fast.next.next  # increment two steps
            slow = slow.next  # increment one step
            prev = prev.next  

        prev.next = slow.next  # when fast hits end (either last node or null) slow becomes middle node
        
        return dummy.next  # return actual head