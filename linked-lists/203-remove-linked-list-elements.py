def removeElements(head, val):
    # use dummy (sentinel) node since head can change (can be deleted)
    dummy = curr = ListNode(next=head)

    # in order not to hold a prev pointer, look ahead by curr.next instead
    while curr.next:
        if curr.next.val == val:  # if equal, delete 
            # do not advance curr pointer since new curr.next might be equal to val
            curr.next = curr.next.next
        else:  # if not equal, proceed
            curr = curr.next

    return dummy.next  # return actual head