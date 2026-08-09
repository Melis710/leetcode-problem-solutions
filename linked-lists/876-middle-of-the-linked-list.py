class Solution:
    ## Two Pointers Solution
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head  # initialize slow and fast pointers 

        while fast and fast.next:  # until fast points to null or fast is the last node
            slow = slow.next  # increment 1 step
            fast = fast.next.next  # increment 2 steps
        
        return slow  # pointer to middle or second middle node