# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Actual Leetcode Solution by Swapping Node Values rather than modifying references
    # time complexity: O(n)
    # space complexity: O(1)
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## find kth node from beginning first
        curr = head  # at index 1
        countdown = k - 1  # to arrive at kth node from head, k-1 steps needed

        while curr and countdown > 0:
            curr = curr.next
            countdown -= 1

        kth_begin = curr  # save kth node from the beginning

        ## find kth node from the end 
        kth_end = head 
        curr = curr.next  # iterate for remaining nodes (n-k) times
        while curr:
            kth_end = kth_end.next
            curr = curr.next

        # once we have kth_begin and kth_end, we can directly swap their value fields
        temp = kth_begin.val
        kth_begin.val = kth_end.val
        kth_end.val = temp
        
        return head  # return the head of the list modified in-place

class Solution2:
    # solution by swapping nodes themselves (pointer manipulation)
    # time complexity: O(n)
    # space complexity: O(1)
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)  # head node itself can change, so use dummy node
        ## find kth node from beginning first
        prev, curr = dummy, head  # prev to link previos node, curr node to find kth node
        countdown = k - 1

        while curr and countdown > 0:
            prev = prev.next
            curr = curr.next
            countdown -= 1

        prev_begin, kth_begin = prev, curr  # save prev and curr

        ## find kth node from the end
        prev_end, kth_end = dummy, head  # initialize previous and current as always 
        # curr we used to find kth node from the beginning, iterate for remaining n-k nodes
        curr = curr.next  
        while curr:
            kth_end = kth_end.next
            prev_end = prev_end.next
            curr = curr.next

        # Early Exit if kth_begin = kth_end
        if kth_begin == kth_end:
            return dummy.next

        # Edge Case 1: Adjacent Nodes - if kth_begin is previous node of kth_end
        # handle this case differently to avoid cycles and infinite loops
        if kth_begin == prev_end:
            prev_begin.next = kth_end
            kth_begin.next = kth_end.next
            kth_end.next = kth_begin
        # Edge Case 2: Adjacent Nodes - if kth_end is previous node of kth_begin
        # handle this case differently to avoid cycles and infinite loops
        elif kth_end == prev_begin:
            prev_end.next = kth_begin
            kth_end.next = kth_begin.next
            kth_begin.next = kth_end
        # standard pointer manipulation for swapping non-adjacent nodes
        else:
            prev_begin.next = kth_end  # connect kth_begin's prev to kth_end
            temp = kth_begin.next  # save kth_begin next before changing it
            kth_begin.next = kth_end.next  # set kth_begin's next to kth_end's next
            prev_end.next = kth_begin  # connect kth_end's prev to kth_begin
            kth_end.next = temp  # set kth_end's next to kth_begin's original next

        return dummy.next  # return new head via dummy node
