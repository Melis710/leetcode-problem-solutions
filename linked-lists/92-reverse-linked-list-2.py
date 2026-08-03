def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)  # dummy node
    curr = dummy

    for _ in range(left-1):
        curr = curr.next
    end = curr  # node just before left
    curr = curr.next  # continue from node at index left
    start = curr  # node at index left 
    prev = None  # standard initialization for reversal
    
    # standard linked list reversal
    for _ in range(right - left + 1):  
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # connect three segments to each other
    start.next = curr
    end.next = prev

    return dummy.next  # return actual head node