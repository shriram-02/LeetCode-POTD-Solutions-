class Solution(object):
    def minScore(self, n, roads):
        g = [[] for _ in range(n+1)]
        for a, b, w in roads:
            g[a].append((b, w))
            g[b].append((a, w))

        seen = [False] * (n+1)
        stack = [1]
        seen[1] = True
        ans = 10**9

        while stack:
            u = stack.pop()
            for v, w in g[u]:
                ans = min(ans, w)
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)

        return ans