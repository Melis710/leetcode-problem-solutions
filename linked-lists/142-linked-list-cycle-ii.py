# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Floyd's Cycle-Finding Algorithm (Hare-Tortoise Algorithm)
    # time complexity: O(n)
    # space complexity: O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head  # initialize slow and fast pointers from the head of list

        while fast and fast.next:  # while we can increment fast pointer 2 steps
            fast = fast.next.next  # increment fast pointer 2 steps    
            slow = slow.next  # increment slow pointer 1 step

            if slow is fast:  # if they meet at the same node in case of a cycle
                slow = head  # start slow from very beginning (distance F to cycle start)
                while slow is not fast:  # increment each 1 step until they meet
                    slow = slow.next
                    fast = fast.next

                return slow  # once two pointers meet at the same node, it's the cycle start

        return None  # if here, no cycle detected   