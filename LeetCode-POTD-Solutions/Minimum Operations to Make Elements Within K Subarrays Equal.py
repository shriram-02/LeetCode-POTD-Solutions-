class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        import heapq

        n = len(nums)
        costs = [0] * (n - x + 1)

        left, right = [], []
        sum_left = sum_right = 0
        size_left = size_right = 0
        delayed = {}

        def prune(heap, sign):
            while heap:
                v = sign * heap[0]
                if delayed.get(v, 0):
                    heapq.heappop(heap)
                    delayed[v] -= 1
                    if delayed[v] == 0:
                        del delayed[v]
                else:
                    break

        def rebalance():
            nonlocal size_left, size_right, sum_left, sum_right

            prune(left, -1)
            prune(right, 1)

            while size_left > size_right + 1:
                prune(left, -1)
                v = -heapq.heappop(left)
                sum_left -= v
                heapq.heappush(right, v)
                sum_right += v
                size_left -= 1
                size_right += 1

            while size_left < size_right:
                prune(right, 1)
                v = heapq.heappop(right)
                sum_right -= v
                heapq.heappush(left, -v)
                sum_left += v
                size_left += 1
                size_right -= 1

            prune(left, -1)
            prune(right, 1)

        def add(v):
            nonlocal size_left, size_right, sum_left, sum_right

            prune(left, -1)
            if not left or v <= -left[0]:
                heapq.heappush(left, -v)
                size_left += 1
                sum_left += v
            else:
                heapq.heappush(right, v)
                size_right += 1
                sum_right += v

            rebalance()

        def remove(v):
            nonlocal size_left, size_right, sum_left, sum_right

            prune(left, -1)

            delayed[v] = delayed.get(v, 0) + 1

            if v <= -left[0]:
                size_left -= 1
                sum_left -= v
            else:
                size_right -= 1
                sum_right -= v

            rebalance()

        for i in range(x):
            add(nums[i])

        costs[0] = get_cost = (
            lambda: (-left[0]) * size_left - sum_left
            + sum_right - (-left[0]) * size_right
        )()

        for i in range(x, n):
            remove(nums[i - x])
            add(nums[i])
            costs[i - x + 1] = (
                (-left[0]) * size_left - sum_left
                + sum_right - (-left[0]) * size_right
            )

        inf = float('inf')
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if j and i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]