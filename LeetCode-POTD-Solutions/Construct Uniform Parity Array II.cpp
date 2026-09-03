class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        length = 0
        odd = False

        for freq in count.values():
            length += (freq // 2) * 2
            if freq % 2:
                odd = True

        return length + (1 if odd else 0)