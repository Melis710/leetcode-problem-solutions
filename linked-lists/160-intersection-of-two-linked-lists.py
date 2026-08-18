# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Solution by:
    # * calculating the length of each lists
    # * determining the longer and shorter one
    # * taking the difference between lengths
    # * advancing longer list by the difference in lengths
    # * traversing both lists simultaneously to find the node where intersection starts

    # time complexity: O(M+N)
    # space complexity: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate length of list A
        lengthA = 0
        curr = headA
        while curr:
            lengthA += 1
            curr = curr.next
        # Calculate length of list B
        lengthB = 0
        curr = headB
        while curr:
            lengthB += 1
            curr = curr.next
        # Determine the longer and shorter lists
        if lengthA > lengthB:
            longer_list = headA
            shorter_list = headB
        else:
            longer_list = headB
            shorter_list = headA
        # Advance the longer list by the difference in lengths
        len_diff = abs(lengthA - lengthB)
        for _ in range(len_diff):
            longer_list = longer_list.next
        # Traverse both lists to find the intersection starting point
        while shorter_list is not longer_list:
            shorter_list = shorter_list.next
            longer_list = longer_list.next

        return shorter_list  # intersection starting node or null if reached the end of list

class Solution2:
    # Clever Solution:
    # Advace both lists simultaneously
    # Eventually shorter one reaches the end, switch it to the beginning of the other list
    # At that point in time, the longer list will have M-N additional nodes to go
    # Since they are advancing together, the other longer one 
    # (one that was traversing the shorter list before) will have gone M-N steps once the original longer list reached the end
    # Hence the original longer list will switch to shorter one
    # At this point in time, two lists are aligned, because the longer list has advanced by the difference in lengths
    # Now continuing the traversal will find the intersection starting node if any 

    # time complexity: O(M+N)
    # space complexity: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1, curr2 = headA, headB  # initialize two pointers for simultaneous traversal

        while curr1 is not curr2:  # while intersection point not found yet or one list reached the end
            # advance original curr1 until it reaches the end, then switch to other list
            curr1 = curr1.next if curr1 else headB
            # advance original curr2 until it reaches the end, then switch to other list
            curr2 = curr2.next if curr2 else headA
        
        return curr1