# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:   
        n = 0  # list length
        # calculate list length
        curr = head
        while curr:
            n += 1
            curr = curr.next

        remainder = n % k  # how many of parts will have one more element
        quotient = n // k  # base number of elements in each part
        res = []  # result of partitions to be returned

        curr = head 
        for _ in range(k):
            n_elements = quotient if not remainder else quotient + 1  # number of elements in a part
            res.append(curr)  # add head of the partitioned linked list
            for _ in range(n_elements-1):  # -1 due to last node needed to set its next to None
                curr = curr.next
            if curr:  # disconnect last node, then increment curr pointer
                temp = curr.next
                curr.next = None
                curr = temp
            if remainder:  # if remainder not 0
                remainder -= 1
           
        return res