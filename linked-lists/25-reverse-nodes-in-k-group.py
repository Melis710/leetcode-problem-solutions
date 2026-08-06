def reverseKGroup(head, k):
    dummy = last_node = ListNode(next=head)  # initialize the last node before the sublist to sort as dummy node
    left_node = right_node = last_node.next  # left_node as start of sublist and temporary right_node for right end 

    while left_node:  # while there is sublist to sort
        # verify k nodes remaining
        for _ in range(k-1):
            if right_node is None:
                break  # less than k nodes -> break
            right_node = right_node.next
        if right_node is None:
            break  # less than k nodes -> break outer loop

        # connect boundaries during sublist reversal
        for _ in range(k-1):
            temp = left_node.next
            last_node.next, left_node.next, temp.next = temp, temp.next, last_node.next

        # shift pointers for next sublist reversal
        last_node = left_node  # when reversed, left_node is rightmost node
        left_node = right_node = last_node.next  # next sublist head node

    return dummy.next  # return actual head node
