# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # since head may change, use a dummy node to handle edge cases
        nums_set = set(nums)  # all unique numbers, use a set for O(1) lookups

        prev, curr = dummy, dummy.next  # initialize 3-node window pointers (next node already accessable by curr.next)
        while curr:
            if curr.val in nums_set:  # if curr deleted don't change prev since new curr also should be deleted in next iteration
                prev.next = curr.next  # disconnect curr 
            else:  # increment prev as normal
                prev = curr
            curr = curr.next  # increment curr pointer in every case 

        return dummy.next  # return actual head of the modified list