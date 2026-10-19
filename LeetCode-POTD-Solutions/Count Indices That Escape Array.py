class Solution:

    def dfs(self, index, arr, state):
        n = len(arr)

        # The current index is outside the array.
        if index < 0 or index >= n:
            return True

        # A zero jump is a dead end.
        if arr[index] == 0:
            return False

        # The index is already known to be good.
        if state[index] == 2:
            return True

        # The index is already known to be bad.
        if state[index] == 3:
            return False

        # A cycle is detected.
        if state[index] == 1:
            return False

        # Mark the current index as visiting.
        state[index] = 1

        # Follow the next index.
        nextIndex = index + arr[index]

        good = self.dfs(nextIndex, arr, state)

        # Store the result for future traversals.
        state[index] = 2 if good else 3

        return good

    def goodIndices(self, arr):
        n = len(arr)
        res = 0

        # 0 = unvisited, 1 = visiting, 2 = good, 3 = bad.
        state = [0] * n

        # Check every index using DFS with memoization.
        for i in range(n):
            if self.dfs(i, arr, state):
                res += 1

        return res
