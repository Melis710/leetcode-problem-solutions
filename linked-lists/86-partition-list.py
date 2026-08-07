## Solution: tracking the last smaller node and once find another smaller node connecting it to the next
class Solution:
    def partition(self, head, x):
        # initialize our prev->curr window, dummy is last_small by default
        prev = last_small = dummy = ListNode(next=head)  # previous node, last smaller node, dummy node
        curr = prev.next

        while curr:  # iterate every node of list
            if curr.val >= x: 
                prev, curr = curr, curr.next  # skip these until smaller value find
            elif last_small.next == curr:  # curr.val < x but it's already in where it should be!
                last_small, prev, curr = curr, curr, curr.next  # update last_small also
            else:  # curr.val < x and curr is within the >= partition, so place it in the < partition
                prev.next, last_small.next, curr.next = curr.next, curr, last_small.next
                last_small, curr = curr, prev.next  # curr should now point to prev's NEW next

        return dummy.next  # return actual list head


## Solution2: accumulating nodes in two separate lists and then connecting both together
class Solution2:
    def partition(self, head, x):
        # create two dummy nodes and initialize tails to connect new nodes
        list1_dummy = list1_tail = ListNode()
        list2_dummy = list2_tail = ListNode()

        while head:  # iterate through the input list
            if head.val < x:  # if value less than x add node to first list
               list1_tail.next = head
               list1_tail = list1_tail.next
            else:  # if value >= x add node to second list
               list2_tail.next = head
               list2_tail = list2_tail.next

            head = head.next  # increment head

        list2_tail.next = None  # set list2.next to null to avoid cycles
        list1_tail.next = list2_dummy.next  # connect list1 to list2

        return list1_dummy.next  # return the actual head node of resulting list 

