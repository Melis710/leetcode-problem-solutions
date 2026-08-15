# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, slow, fast = dummy, head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next

        prev.next = slow.next
        
        return dummy.next