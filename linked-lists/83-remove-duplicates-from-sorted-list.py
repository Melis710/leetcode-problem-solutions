# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # We have a current node and at each iteration we compare it to its next node.
    # If its next node has the same value, delete the next node.
    # Otherwise, increment the pointer one step to repeat the same process with another value.

    # time complexity: O(n)
    # space complexity: O(1)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head