class Solution(object):
    def lengthOfLongestSubstring(self, s):
        used = {}
        index = 0
        max_length = 0

        for i, c in enumerate(s):
            if c in used and index <= used[c]:
                index = used[c] + 1
            else:
                max_length = max(max_length, i - index + 1) 
            used[c] = i

        return(max_length)

