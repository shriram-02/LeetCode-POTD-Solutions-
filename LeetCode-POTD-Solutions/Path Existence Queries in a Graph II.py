class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))
        vals = [x[0] for x in arr]
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        nxt = [0] * n
        r = 0
        for i in range(n):
            while r + 1 < n and vals[r + 1] - vals[i] <= maxDiff:
                r += 1
            nxt[i] = r

        LOG = n.bit_length()
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu, pv = pos[u], pos[v]
            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            if pu > pv:
                pu, pv = pv, pu

            cur = pu
            steps = 0
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < pv:
                    cur = up[k][cur]
                    steps += 1 << k
            ans.append(steps + 1)

        return ans