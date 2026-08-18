# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative Solution
    # time complexity: O(n)
    # space complexity: O(1)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # head node may have duplicates, need a valid head node
        prev, curr = dummy, head  # prev pointer for new links, curr for current node

        while curr and curr.next:  # while at least one another node to compare with
            if curr.val == curr.next.val:  # if duplication detected, skip nodes with the same value
                dup_val = curr.val  # save duplicate value to compare with current node's
                while curr and curr.val == dup_val:  # until curr has a different value, skip it
                    curr = curr.next
                prev.next = curr  # connect prev to the new node with a different value
            else:  # if current node has a unique value, simply advance both prev and curr
                prev = prev.next
                curr = curr.next
            
        return dummy.next  # return new head