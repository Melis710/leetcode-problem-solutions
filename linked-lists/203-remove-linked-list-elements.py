def removeElements(head, val):
    dummy = curr = ListNode(next=head)

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next