def lengthOfLongestSubstring(s: str) -> int:
    left = 0  # left pointer of window
    last_seen = dict()  # last seen index of a character
    longest = 0  # longest length

    for right, char in enumerate(s):  # right pointer of window and current character
        if last_seen.get(char, -1) >= left:  # char was already within the window?
            left = last_seen[char] + 1  # shrink the window to skip the old duplicate

        last_seen[char] = right  # update the last seen index for the current character
        longest = max(longest, right-left+1)  # update the longest length

    return longest
