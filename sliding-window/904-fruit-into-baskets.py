class Solution:
    # Dynamically sized sliding window using hashmap (common template for this problem)
    # scalable to any number of baskets
    # time complexity: O(n)
    # space complexity: O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2  # number of baskets given in the problem definition
        freq_map = dict()  # frequency map for the numbers within the window
        left = 0  # left boundary of the window
        max_len = 0  # maximum length (maximum total number of fruits in all baskets)

        for right, fruit in enumerate(fruits):  # right boundary (included), fruit type
            freq_map[fruit] = freq_map.get(fruit, 0) + 1  # expand window to the right
            # shrink window from left if number of fruit types doesn't fit into baskets
            while len(freq_map) > k:
                freq_map[fruits[left]] -= 1
                if not freq_map[fruits[left]]:
                    del freq_map[fruits[left]]
                left += 1
            # after adjusting window to make it valid, update the maximum length
            max_len = max(max_len, right - left + 1)

        return max_len

class Solution:
    # State management through fixed number of variables
    # tightly bound to the specific number of baskets given in this problem, non-scalable solution
    # time complexity: O(n)
    # space complexity: O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        # initialize two fruit types and their start indices 
        a, b = fruits[0], None
        idx_a, idx_b = 0, None  # represent the start of last blocks of consecutive fruits of same type
        length = 0
        for f in fruits:
            length += 1
            if f != a:
                b = f
                break

        if b is None:  # there's only one type, return the length
            return length

        idx_b = length - 1  # 0-based indexing
        max_length = length  # initialize maximum length as the current length
        # process the remaining list
        for i in range(idx_b+1, len(fruits)):
            # if new fruit is of type a and previous one is of b, update a's last block start
            if fruits[i] == a and fruits[i-1] == b:   
                idx_a = i
            # if new fruit is of type b and previous one is of a, update b's last block start
            elif fruits[i] == b and fruits[i-1] == a:
                idx_b = i
            # new fruit is a third type, set it as new 'a' or 'b'
            # whichever is the previous block 
            # since the previous block's type will no longer be used
            else:
                if idx_a > idx_b:  # a is our last block and we continue to use it
                    # change the b to the new fruit type
                    b = fruits[i]
                    idx_b = i
                    length = i - idx_a
                else:  # idx_a < idx_b, b is our last block and we continue to use it
                    # change the a to the new fruit type
                    a = fruits[i] 
                    idx_a = i
                    length = i - idx_b
                    
            length += 1  # in any case above, the length must be incremented by 1
            max_length = max(max_length, length)  # update the maximum length after all adjustments

        return max_length
