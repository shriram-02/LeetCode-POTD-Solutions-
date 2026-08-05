class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        def dfs(u):
            suspicious[u] = True
            for v in graph[u]:
                if not suspicious[v]:
                    dfs(v)

        dfs(k)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]