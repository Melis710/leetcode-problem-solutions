# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # in-place solution
    # time complexity: O(n)
    # space complexity: O(1) 
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the list
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        # filter some nodes so that the remaining nodes will be in non-decreasing order
        last_max = prev
        curr = prev.next
        while curr:
            if curr.val >= last_max.val:
                last_max.next = curr
                last_max = curr
            curr = curr.next
        last_max.next = None

        # reverse the resulting list back
        prev, curr = None, prev
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev  # return new head

class Solution2:
    # Monotonic Stack solution
    # time complexity: O(n)
    # space complexity: O(n)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # build a stack of non-ascending nodes
        stack = []
        curr = head
        while curr:
            # until the last node has no node with a greater value in the right side (curr)
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)  # push new node 
            curr = curr.next

        # reconnect the nodes in the stack
        for i in range(len(stack)-1):
            stack[i].next = stack[i+1] 
        stack[-1].next = None  # set the tail

        return stack[0]  # return head