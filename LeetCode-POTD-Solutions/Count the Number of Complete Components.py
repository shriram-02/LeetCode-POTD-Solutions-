from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        vis = [False] * n
        ans = 0

        def dfs(node):
            vis[node] = True
            comp.append(node)
            for nei in graph[node]:
                if not vis[nei]:
                    dfs(nei)

        for i in range(n):
            if not vis[i]:
                comp = []
                dfs(i)

                k = len(comp)
                edge_count = sum(len(graph[node]) for node in comp)

                if edge_count == k * (k - 1):
                    ans += 1

        return ans