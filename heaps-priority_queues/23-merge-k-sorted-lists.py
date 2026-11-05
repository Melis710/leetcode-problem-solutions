# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    # Min Heap solution
    # IMPORTANT TRICK: Python checks second element when comparing tuples to put into heap 
    # and since ListNode does not support < operator by default, we should add a second 
    # unique index as second element of tuple
    
    # time complexity: O(N*logK)
    # space complexity: O(K)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, idx, l))

        dummy_node = ListNode()
        curr = dummy_node
        
        while min_heap:
            _, idx, min_head = heapq.heappop(min_heap)
            curr.next = min_head
            curr = curr.next
            if min_head.next:
                heapq.heappush(min_heap, (min_head.next.val, idx, min_head.next))
        
        return dummy_node.next
