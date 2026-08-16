# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []  # result to be returned
        stack = []  # monotonically decreasing stack
        curr = head  # current node pointer to traverse linked list
        idx = 0  # index with which the node values are stored in stack to protect order
        while curr:
            res.append(0)  # increase list size to allocate a list of size n in total

            while stack and stack[-1][1] < curr.val:
                i, _ = stack.pop()  # extract index to put its greater value into correct place
                res[i] = curr.val  # set the greater value of number at index i

            stack.append((idx, curr.val))  # push current value onto the stack to find its greater value
            idx += 1
            curr = curr.next

        return res