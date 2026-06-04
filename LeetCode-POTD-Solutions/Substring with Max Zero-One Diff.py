class Solution:
    def maxSubstring(self, s):
        max_ending = 0
        max_so_far = float('-inf')
        
        for ch in s:
            val = 1 if ch == '0' else -1
            max_ending = max(val, max_ending + val)
            max_so_far = max(max_so_far, max_ending)
        
        return -1 if max_so_far <= 0 else max_so_far