class Solution {
public:
    vector<int> findWays(vector<vector<int>>& grid) {
        const int MOD = 1000000007;
        int n = grid.size();

        vector<vector<int>> paths(n, vector<int>(n, 0));
        vector<vector<int>> best(n, vector<int>(n, 0));

        paths[0][0] = 1;
        best[0][0] = grid[0][0];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0)
                    continue;

                if (i > 0 && (grid[i - 1][j] == 2 || grid[i - 1][j] == 3)) {
                    paths[i][j] = (paths[i][j] + paths[i - 1][j]) % MOD;

                    if (paths[i - 1][j] > 0) {
                        best[i][j] = max(
                            best[i][j],
                            best[i - 1][j] + grid[i][j]
                        );
                    }
                }

                if (j > 0 && (grid[i][j - 1] == 1 || grid[i][j - 1] == 3)) {
                    paths[i][j] = (paths[i][j] + paths[i][j - 1]) % MOD;

                    if (paths[i][j - 1] > 0) {
                        best[i][j] = max(
                            best[i][j],
                            best[i][j - 1] + grid[i][j]
                        );
                    }
                }
            }
        }

        return {paths[n - 1][n - 1], best[n - 1][n - 1]};
    }
};