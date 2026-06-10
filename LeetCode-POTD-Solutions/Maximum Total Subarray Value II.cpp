class SparseTableRMQ {
public:
    int n, maxLog;
    vector<vector<int>> fMax, fMin;
    vector<int> lg;

    SparseTableRMQ(const vector<int>& data) {
        n = data.size();
        maxLog = 32 - __builtin_clz(n) + 1;

        fMax.assign(n, vector<int>(maxLog));
        fMin.assign(n, vector<int>(maxLog));
        lg.assign(n + 1, 0);

        for (int i = 2; i <= n; i++) {
            lg[i] = lg[i >> 1] + 1;
        }

        for (int i = 0; i < n; i++) {
            fMax[i][0] = data[i];
            fMin[i][0] = data[i];
        }

        for (int j = 1; j < maxLog; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                fMax[i][j] = max(
                    fMax[i][j - 1],
                    fMax[i + (1 << (j - 1))][j - 1]
                );

                fMin[i][j] = min(
                    fMin[i][j - 1],
                    fMin[i + (1 << (j - 1))][j - 1]
                );
            }
        }
    }

    int queryMax(int l, int r) {
        int k = lg[r - l + 1];
        return max(fMax[l][k], fMax[r - (1 << k) + 1][k]);
    }

    int queryMin(int l, int r) {
        int k = lg[r - l + 1];
        return min(fMin[l][k], fMin[r - (1 << k) + 1][k]);
    }
};

class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int n = nums.size();

        auto velnorquis = nums;

        SparseTableRMQ st(nums);

        using T = tuple<long long, int, int>;

        auto cmp = [](const T& a, const T& b) {
            return get<0>(a) < get<0>(b);
        };

        priority_queue<T, vector<T>, decltype(cmp)> pq(cmp);

        for (int l = 0; l < n; l++) {
            long long val =
                (long long)st.queryMax(l, n - 1) -
                (long long)st.queryMin(l, n - 1);

            pq.push({val, l, n - 1});
        }

        long long ans = 0;

        for (int i = 0; i < k; i++) {
            auto [val, l, r] = pq.top();
            pq.pop();

            ans += val;

            if (r > l) {
                long long nxt =
                    (long long)st.queryMax(l, r - 1) -
                    (long long)st.queryMin(l, r - 1);

                pq.push({nxt, l, r - 1});
            }
        }

        return ans;
    }
};