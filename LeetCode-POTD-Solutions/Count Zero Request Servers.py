class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])
        sorted_queries = sorted(enumerate(queries), key=lambda a: a[1])

        ans = [0] * len(queries)
        count = {}
        left = right = 0

        for idx, q in sorted_queries:
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                count[server] -= 1
                if count[server] == 0:
                    del count[server]
                left += 1

            ans[idx] = n - len(count)

        return ans