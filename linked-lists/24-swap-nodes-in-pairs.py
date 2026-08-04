def swapPairs(head):
    dummy = ListNode(next=head)
    prev = dummy  # connect swapped pair to previous part of list
    curr = head

    while curr and curr.next:  # process in pairs
        # save pointers before changing
        next_node = curr.next
        next_next = next_node.next  # next node of next_node

        # swap
        prev.next = next_node  # make prev point to curr's next
        next_node.next = curr  # make next of curr's point to curr
        curr.next = next_next  # make curr point to next node of "curr's next"

        # shift pair
        prev = curr
        curr = next_next

    return dummy.next  # return actual head