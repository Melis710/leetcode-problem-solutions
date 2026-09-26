class Solution:
    # hashmap solution
    # time complexity: O(N*K), where N is number of strings and K is length of word
    # space complexity: O(N) for N unique anagram keys with O(1) 26-char sized tuples  
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = dict()  # accumulate the anagram groups, key: tuple value: list

        for word in strs:
            char_freq = [0]*26  # frequency array, index 26 english lowercase characters
            for char in word:
                char_freq[ord(char) - ord('a')] += 1  # increment count at alphabet position
            key = tuple(char_freq)  # convert it into immutable hashable tuple
            if key in groups:  # if group already exists, append the word to that group
                groups[key].append(word)
            else:  # create the new group initializing with this word
                groups[key] = [word]

        return list(groups.values())  # return the list of groups