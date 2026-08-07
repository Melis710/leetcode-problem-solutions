def oddEvenList(head):
    # partition into two linked lists 
    odds, evens = head, head.next if head else None  # initialize odd and even list heads
    evens_head = evens  # needed to reconnect

    # since evens is initialized a step ahead of odds, continue from there
    while evens and evens.next:
        odds.next = evens.next  # evens.next is an odd
        odds = odds.next  # increment odds tail
        evens.next = odds.next  # odds.next is equal to evens.next.next which is even (or None)
        evens = evens.next  # increment evens tail

    if odds:  # if we have a non-empty list
        odds.next = evens_head  # connect lists together

    return head  # head remains unchanged