from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = sorted(Counter(word).values(), reverse=True)

        ans = 0
        for i, f in enumerate(freq):
            ans += (i // 8 + 1) * f

        return ans