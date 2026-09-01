class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size();
        int n = classroom[0].size();

        int sr = -1, sc = -1;
        int cnt = 0;

        // Give each litter an ID for bitmask
        vector<vector<int>> id(m, vector<int>(n, -1));

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(classroom[i][j] == 'S'){
                    sr = i;
                    sc = j;
                }
                if(classroom[i][j] == 'L'){
                    id[i][j] = cnt++;
                }
            }
        }

        int masks = 1 << cnt;
        int fullMask = masks - 1;

        // best[r][c][mask] = max energy reached at this state
        vector<vector<vector<int>>> best(
            m,
            vector<vector<int>>(
                n,
                vector<int>(masks, -1)
            )
        );

        struct State {
            int r, c;
            int mask;
            int en;
            int dist;
        };

        queue<State> q;
        q.push({sr, sc, 0, energy, 0});
        best[sr][sc][0] = energy;

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        while(!q.empty()){
            State cur = q.front();
            q.pop();

            int r = cur.r;
            int c = cur.c;
            int mask = cur.mask;
            int en = cur.en;
            int dist = cur.dist;

            // All litter collected
            if(mask == fullMask){
                return dist;
            }
            // No energy, cannot move
            if(en == 0){
                continue;
            }

            for(int d = 0; d < 4; d++){
                int nr = r + dr[d];
                int nc = c + dc[d];

                // Outside grid
                if(nr < 0 || nr >= m || nc < 0 || nc >= n){
                    continue;
                }

                // Obstacle
                if(classroom[nr][nc] == 'X'){
                    continue;
                }

                int newEn = en - 1;
                int newMask = mask;

                // Collect litter
                if(classroom[nr][nc] == 'L'){
                    newMask |= (1 << id[nr][nc]);
                }

                // Recharge
                if(classroom[nr][nc] == 'R'){
                    newEn = energy;
                }

                // Already reached with more energy
                if(best[nr][nc][newMask] >= newEn){
                    continue;
                }

                best[nr][nc][newMask] = newEn;
                q.push({nr, nc, newMask, newEn, dist + 1});
            }
        }
        return -1;
    }
};