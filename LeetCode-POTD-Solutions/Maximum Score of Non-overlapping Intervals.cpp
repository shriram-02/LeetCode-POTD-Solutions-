class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        
        vector<array<long long, 4>> dp(n + 1);
        vector<array<vector<int>, 4>> paths(n + 1);
        
        vector<array<long long, 4>> best(n + 1);
        vector<array<vector<int>, 4>> bestPath(n + 1);
        
        vector<int> ord(n);
        iota(ord.begin(), ord.end(), 0);
        
        sort(ord.begin(), ord.end(), [&](int a, int b) {
            if (intervals[a][1] != intervals[b][1])
                return intervals[a][1] < intervals[b][1];
            return a < b;
        });
        
        vector<int> ends(n);
        for (int i = 0; i < n; ++i)
            ends[i] = intervals[ord[i]][1];
        
        auto better = [&](long long w1, const vector<int>& p1,
                          long long w2, const vector<int>& p2) {
            if (w1 != w2) return w1 > w2;
            return p1 < p2;
        };
        
        vector<vector<long long>> val(n + 1, vector<long long>(5, 0));
        vector<vector<vector<int>>> take(n + 1, vector<vector<int>>(5));
        
        for (int i = 1; i <= n; ++i) {
            int idx = ord[i - 1];
            int l = intervals[idx][0];
            long long w = intervals[idx][2];
            
            int p = lower_bound(ends.begin(), ends.end(), l) - ends.begin();
            
            for (int k = 0; k <= 4; ++k) {
                val[i][k] = val[i - 1][k];
                take[i][k] = take[i - 1][k];
            }
            
            for (int k = 1; k <= 4; ++k) {
                long long nw = val[p][k - 1] + w;
                vector<int> np = take[p][k - 1];
                np.push_back(idx);
                sort(np.begin(), np.end());
                
                if (better(nw, np, val[i][k], take[i][k])) {
                    val[i][k] = nw;
                    take[i][k] = np;
                }
            }
        }
        
        vector<int> ans;
        long long bestWeight = -1;
        
        for (int k = 0; k <= 4; ++k) {
            if (better(val[n][k], take[n][k], bestWeight, ans)) {
                bestWeight = val[n][k];
                ans = take[n][k];
            }
        }
        
        return ans;
    }
};