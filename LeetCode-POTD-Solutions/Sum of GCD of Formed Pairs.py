from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        pref = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            pref.append(gcd(x, mx))

        pref.sort()

        ans = 0
        i, j = 0, len(pref) - 1
        while i < j:
            ans += gcd(pref[i], pref[j])
            i += 1
            j -= 1

        return ans