from dataclasses import dataclass
from itertools import pairwise

@dataclass
class Group:
    start: int
    length: int


class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        self.st = [[0] * (self.n + 1) for _ in range(self.n.bit_length() + 1)]
        self.st[0] = nums[:]
        for i in range(1, self.n.bit_length() + 1):
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(
                    self.st[i - 1][j],
                    self.st[i - 1][j + (1 << (i - 1))]
                )

    def query(self, l, r):
        k = (r - l + 1).bit_length() - 1
        return max(self.st[k][l], self.st[k][r - (1 << k) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')
        zeroGroups, zeroGroupIndex = self._getZeroGroups(s)

        if not zeroGroups:
            return [ones] * len(queries)

        st = SparseTable(self._getZeroMergeLengths(zeroGroups))

        def solve(l, r):
            left = -1 if zeroGroupIndex[l] == -1 else (
                zeroGroups[zeroGroupIndex[l]].length -
                (l - zeroGroups[zeroGroupIndex[l]].start)
            )
            right = -1 if zeroGroupIndex[r] == -1 else (
                r - zeroGroups[zeroGroupIndex[r]].start + 1
            )

            startAdj = zeroGroupIndex[l] + 1
            endAdj = (zeroGroupIndex[r] if s[r] == '1' else zeroGroupIndex[r] - 1) - 1

            ans = ones

            if (
                s[l] == '0' and s[r] == '0' and
                zeroGroupIndex[l] + 1 == zeroGroupIndex[r]
            ):
                ans = max(ans, ones + left + right)
            elif startAdj <= endAdj:
                ans = max(ans, ones + st.query(startAdj, endAdj))

            if (
                s[l] == '0' and
                zeroGroupIndex[l] + 1 <=
                (zeroGroupIndex[r] if s[r] == '1' else zeroGroupIndex[r] - 1)
            ):
                ans = max(ans, ones + left + zeroGroups[zeroGroupIndex[l] + 1].length)

            if (
                s[r] == '0' and
                zeroGroupIndex[l] < zeroGroupIndex[r] - 1
            ):
                ans = max(ans, ones + right + zeroGroups[zeroGroupIndex[r] - 1].length)

            return ans

        return [solve(l, r) for l, r in queries]

    def _getZeroGroups(self, s):
        groups = []
        idx = []
        for i, ch in enumerate(s):
            if ch == '0':
                if i and s[i - 1] == '0':
                    groups[-1].length += 1
                else:
                    groups.append(Group(i, 1))
            idx.append(len(groups) - 1)
        return groups, idx

    def _getZeroMergeLengths(self, groups):
        return [a.length + b.length for a, b in pairwise(groups)]