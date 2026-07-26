def longestOnes(nums: list[int], k: int) -> int:
    n = len(nums)
    i = 0  # left pointer
    zeros = 0  # number of zeros within the window

    for j in range(n):  # right pointer
        if nums[j] == 0:  # increment zero counter
            zeros += 1

        if zeros > k:  # if number of zeros > k, shift window to right
            if nums[i] == 0:  # update number of zeros within the shifted window
                zeros -= 1
            i += 1 

    return n - i  # window length   
