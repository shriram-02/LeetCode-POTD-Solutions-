from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        m = len(s)
        pref_cnt = [0] * (m + 1)

        digits = []
        pref_sum = [0]
        pref_val = [0]
        pow10 = [1]

        for i, ch in enumerate(s):
            pref_cnt[i + 1] = pref_cnt[i]
            if ch != '0':
                d = ord(ch) - ord('0')
                pref_cnt[i + 1] += 1
                digits.append(d)
                pref_sum.append(pref_sum[-1] + d)
                pow10.append((pow10[-1] * 10) % MOD)
                pref_val.append((pref_val[-1] * 10 + d) % MOD)

        ans = []

        for l, r in queries:
            left = pref_cnt[l]
            right = pref_cnt[r + 1] - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1
            x = (pref_val[right + 1] - pref_val[left] * pow10[length]) % MOD
            sm = pref_sum[right + 1] - pref_sum[left]
            ans.append((x * sm) % MOD)

        return ans