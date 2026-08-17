# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Floyd's Cycle-Finding Algorithm (Hare-Tortoise Algorithm) solution
    # time complexity: O(n)
    # space complexity: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head  # initialize slow and fast pointers from the head of list

        while fast and fast.next:  # while we can increment fast pointer two steps
            fast = fast.next.next  # increment fast pointer two steps
            slow = slow.next  # increment slow pointer one step

            if fast is slow:  # if fast and slow references same object in memory
                return True  # cycle detected

        return False  # no cycle detected

class Solution2:
    # solution via hash set
    # time complexity: O(n)
    # space complexity: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = set()  # create a hashset for nodes seen during traversal
        
        while head:
            if head in seen_nodes:  # if current node seen before, cycle detected
                return True
            
            seen_nodes.add(head)  # add new node visited to seen nodes
            head = head.next  # increment current node pointer 

        return False  # if here, no cycle detected

                    