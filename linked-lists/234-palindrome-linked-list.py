def isPalindrome(head):
    slow = fast = head  # slow holds second half
    reversed_half = None  # first half

    # find the middle and reverse the first half
    while fast and fast.next:
        fast = fast.next.next  # 2 steps forward
        # reverse slow pointer and increment slow
        slow.next, reversed_half, slow = reversed_half, slow, slow.next

    # handle odd-length lists 
    if fast:  # if fast is not None, the length is odd
        slow = slow.next  # skip the middle since it has no effect for palindrome

    # compare the two halves
    while slow and slow.val == reversed_half.val:
        slow = slow.next
        reversed_half = reversed_half.next 

    return not slow  # expect slow to be None
    