def find_subarray_sum(nums: list[int], target_sum: int) -> list[int]:
    n = len(nums)
    if n == 0:
        return [-1, -1]
    if n == 1:
        return [0, 0] if nums[0] == target_sum else [-1, -1]
    i, j = 0, 0
    win_sum = nums[i]
    while i <= j and j < n: 
        if win_sum < target_sum:
            j += 1
            win_sum += nums[j]
        elif win_sum == target_sum:
            return [i, j]
        else:  # win_sum > target_sum:
            win_sum -= nums[i]
            i += 1

    return [-1, -1]


def find_subarray_sum2(nums: list[int], target_sum: int) -> list[int]:
    i = 0
    win_sum = 0
    for j in range(len(nums)):
        win_sum += nums[j]
        while win_sum > target_sum:
            win_sum -= nums[i]
            i += 1
        if win_sum == target_sum:
            return [i, j]
    return [-1, -1]

def longest_subarray_sum(nums: list[int], target_sum: int) -> list[int]:
    i = 0
    win_sum = 0
    max_size = float('-inf')

    for j in range(len(nums)):
        win_sum += nums[j]
        while win_sum > target_sum:
            win_sum -= nums[i]
            i += 1
        if win_sum == target_sum:
            max_size = max(max_size, j - i + 1)

    return max_size


def longest_unique_substring(s: str):
    # return length of the longest substring containing only unique chars
    win_set = set()  # window set
    max_len = 0  # longest length
    i = 0
    
    for j in range(len(s)):
        while s[j] in win_set:
            win_set.remove(s[i])
            i += 1
        win_set.add(s[j])
        max_len = max(max_len, j - i + 1)

    return max_len
'''
print(longest_unique_substring("abcabcqbb"))  # 4
print(longest_subarray_sum([1, 2, 3], 7))
print(find_subarray_sum2([0, 1, 3, 5], target_sum=5))
'''

def less_than_k(nums, k):
    if k <= 1:
        return 0
    
    i = 0
    product = 1
    total = 0

    for j in range(len(nums)):
        product *= nums[j]
        while product >= k:
            product //= nums[i]
            i += 1
        total += (j - i + 1)
        
    return total
print(less_than_k([1, 1, 1, 1], 2))
print(5 & 1)