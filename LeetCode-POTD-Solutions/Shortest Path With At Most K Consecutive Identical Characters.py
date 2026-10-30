class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        import heapq

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        # State: (node, last character, consecutive count)
        pq = [(0, 0, labels[0], 1)]
        dist = {}

        while pq:
            cost, node, last, count = heapq.heappop(pq)

            state = (node, last, count)

            if cost > dist.get(state, float('inf')):
                continue

            if node == n - 1:
                return cost

            for nei, weight in adj[node]:
                if labels[nei] == last:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_state = (nei, labels[nei], new_count)
                new_cost = cost + weight

                if new_cost < dist.get(new_state, float('inf')):
                    dist[new_state] = new_cost
                    heapq.heappush(
                        pq,
                        (new_cost, nei, labels[nei], new_count)
                    )

        return -1