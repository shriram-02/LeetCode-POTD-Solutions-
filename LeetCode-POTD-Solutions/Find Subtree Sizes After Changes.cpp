class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);

        for (int i = 1; i < n; i++) {
            adj[parent[i]].push_back(i);
        }

        vector<int> last(26, -1);
        vector<int> newParent(n, -1);

        function<void(int)> dfs = [&](int u) {
            int c = s[u] - 'a';
            int prev = last[c];

            if (prev != -1)
                newParent[u] = prev;
            else
                newParent[u] = parent[u];

            last[c] = u;

            for (int v : adj[u]) {
                dfs(v);
            }

            last[c] = prev;
        };

        dfs(0);

        vector<vector<int>> newAdj(n);

        for (int i = 1; i < n; i++) {
            newAdj[newParent[i]].push_back(i);
        }

        vector<int> ans(n, 1);

        function<int(int)> dfs2 = [&](int u) {
            for (int v : newAdj[u]) {
                ans[u] += dfs2(v);
            }
            return ans[u];
        };

        dfs2(0);

        return ans;
    }
};