def isValid(s: str) -> bool:
    stack = []  # left brackets added to stack
    left_brac = {'{': '}', '(': ')', '[': ']'}  # left-right bracket pairs

    for char in s:
        if char in left_brac:  # left bracket?
            stack.append(char)
        else:  # right bracket
            if not stack:  # there is no left bracket to compare at all?
                return False
            left = stack.pop()  # get last left bracket
            if left_brac[left] != char:  # no correspondence?
                return False
    
    return not stack  # all left brackets have a match?