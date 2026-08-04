from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse(head:Optional[ListNode]) -> None:
    curr = head
    print("[", end="")

    while curr:
        print(str(curr.val) + ", ", end="")
        curr = curr.next

    print("]")

class Solution:
    def mergeTwoLists(self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()  # dummy node
        curr = head  # current node to build merged list

        while list1 and list2:  # O(min(M, N))
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:  # list2 <= list1
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2  # append the remaining 
        return head.next  # return actual head node

def main():
    # sorted list1: [1, 1, 2, 14, 14, 21]
    node5 = ListNode(21, None)
    node4 = ListNode(14, node5)
    node3 = ListNode(14, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    node0 = ListNode(1, node1)
    list1 = node0

    # sorted list2: [2, 3, 3, 18]
    node3 = ListNode(18, None)
    node2 = ListNode(3, node3)
    node1 = ListNode(3, node2)
    node0 = ListNode(2, node1)
    list2 = node0

    # traverse lists before merge them
    traverse(list1)
    traverse(list2)

    # merge two sorted lists
    head = Solution().mergeTwoLists(list1, list2)

    # traverse the merged list
    traverse(head)

if __name__ == "__main__":
    main()