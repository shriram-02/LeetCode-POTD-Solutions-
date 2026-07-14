from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        M = 200

        g = [[0] * (M + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            for j in range(M + 1):
                if i == 0:
                    g[i][j] = j
                elif j == 0:
                    g[i][j] = i
                else:
                    g[i][j] = gcd(i, j)

        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [row[:] for row in dp]
            for a in range(M + 1):
                for b in range(M + 1):
                    if dp[a][b] == 0:
                        continue
                    ndp[g[a][x]][b] = (ndp[g[a][x]][b] + dp[a][b]) % MOD
                    ndp[a][g[b][x]] = (ndp[a][g[b][x]] + dp[a][b]) % MOD
            dp = ndp

        ans = 0
        for i in range(1, M + 1):
            ans = (ans + dp[i][i]) % MOD
        return ans