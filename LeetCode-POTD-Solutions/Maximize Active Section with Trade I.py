class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        t = '1' + s + '1'
        
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        ans = ones
        for k in range(1, len(runs) - 1):
            if (
                runs[k][0] == '1'
                and runs[k - 1][0] == '0'
                and runs[k + 1][0] == '0'
            ):
                ans = max(ans, ones + runs[k - 1][1] + runs[k + 1][1])

        return ans