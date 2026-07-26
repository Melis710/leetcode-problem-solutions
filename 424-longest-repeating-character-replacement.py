def characterReplacement(s: str, k: int) -> int:
    i = 0  # left pointer to shift window (not shrink)
    char_freq = dict()
    max_freq = 0

    for j in range(len(s)):  # right pointer to expand window
        char_freq[s[j]] = char_freq.get(s[j], 0) + 1
        max_freq = max(max_freq, char_freq[s[j]])  # update max frequency
        
        if (j - i + 1) - max_freq > k:  # if window size - max char frequency > k
            char_freq[s[i]] -= 1  # shift the window to the right
            i += 1

    return len(s) - i  # window size
