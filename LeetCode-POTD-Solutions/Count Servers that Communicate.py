class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = [sum(row) for row in grid]  # servers on each row
        cols = [sum(col) for col in zip(*grid)]  # servers on each column

        ans = 0
        for i, row in enumerate(grid):
            for j, server in enumerate(row):
                if server and rows[i] + cols[j] > 2:  # it's counted in both, so more than 2 means company
                    ans += 1
        return ans