class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        long long lo = 1, hi = 1LL * coins[0] * k;

        auto count = [&](long long x) {
            long long res = 0;
            int n = coins.size();

            for (int mask = 1; mask < (1 << n); ++mask) {
                long long lcm = 1;
                int bits = 0;
                bool overflow = false;

                for (int i = 0; i < n; ++i) {
                    if (mask & (1 << i)) {
                        ++bits;
                        long long g = std::gcd(lcm, (long long)coins[i]);
                        lcm = lcm / g * coins[i];

                        if (lcm > x) {
                            overflow = true;
                            break;
                        }
                    }
                }

                if (!overflow) {
                    long long cnt = x / lcm;
                    if (bits & 1) res += cnt;
                    else res -= cnt;
                }
            }

            return res;
        };

        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;

            if (count(mid) >= k)
                hi = mid;
            else
                lo = mid + 1;
        }

        return lo;
    }
};