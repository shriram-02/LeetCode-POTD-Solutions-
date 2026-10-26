
class Solution {
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        int ans = 0;
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        int dx[] = {1, -1, 0, 0};
        int dy[] = {0, 0, 1, -1};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 || visited[i][j])
                    continue;

                long long sum = 0;
                queue<pair<int, int>> q;
                q.push({i, j});
                visited[i][j] = true;

                while (!q.empty()) {
                    auto [x, y] = q.front();
                    q.pop();
                    sum += grid[x][y];

                    for (int d = 0; d < 4; d++) {
                        int nx = x + dx[d];
                        int ny = y + dy[d];

                        if (nx >= 0 && nx < m && ny >= 0 && ny < n &&
                            grid[nx][ny] > 0 && !visited[nx][ny]) {
                            visited[nx][ny] = true;
                            q.push({nx, ny});
                        }
                    }
                }

                if (sum % k == 0)
                    ans++;
            }
        }

        return ans;
    }
};
