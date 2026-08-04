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
    def removeNthFromEnd(self, head:Optional[ListNode], n:int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast, slow = dummy, dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

def main():
    # List: [6, 0, 12, 45, 23, 7, ]
    node5 = ListNode(7, None)
    node4 = ListNode(23, node5)
    node3 = ListNode(45, node4)
    node2 = ListNode(12, node3)
    node1 = ListNode(0, node2)
    node0 = ListNode(6, node1)

    # print the list before deleting n = 2rd node from end of list
    traverse(node0)

    # delete the 2rd node from end (n=2)
    Solution().removeNthFromEnd(node0, n=2)

    # print the list after deleting 2rd node from end of list
    traverse(node0)

if __name__ == "__main__":
    main()
