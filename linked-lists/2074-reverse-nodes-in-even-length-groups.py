# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 2  # anticipated group length, initialize as 2 for first even group 
        curr = head.next  # start from first even group
        last_node = head  # last_node of previous reversed group

        while curr:  # as long as new group is not empty
            start_node = curr  # save curr node as start_node of new group
            ## Calculate actual length of new group
            n = 0  # actual length 
            while curr and n < length:
                curr = curr.next
                n += 1
            # if new group has even numbers of nodes, reverse it
            if n % 2 == 0:
                # set prev, re-set curr
                prev, curr = start_node, start_node.next
                for _ in range(n-1):  # at the end, curr points to first node of new group
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node
                # reconnect new reversed group at the boundaries
                start_node.next = curr
                last_node.next = prev
                # start_node of the reversed group becomes the last_node for the next group
                last_node = start_node
            else:
                # length is odd, just walk last_node to the end of the current group
                for _ in range(n):
                    last_node = last_node.next
            # increment anticipated group length for the next iteration
            length += 1

        return head