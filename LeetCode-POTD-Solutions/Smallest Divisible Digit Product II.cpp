constexpr uint8_t GCD[10][10] = {
    {},
    {1},
    {2, 1},
    {3, 1, 1},
    {4, 1, 2, 1},
    {5, 1, 1, 1, 1},
    {6, 1, 2, 3, 2, 1},
    {7, 1, 1, 1, 1, 1, 1},
    {8, 1, 2, 1, 4, 1, 2, 1},
    {9, 1, 1, 3, 1, 1, 3, 1, 1},
};

constexpr int MAXN = 200'001;
long long rem[MAXN];
char buf[MAXN + 1];

class Solution {
public:
    string smallestNumber(string num, long long t) {
        long long temp = t >> __builtin_ctzll(t);
        for (int i : {3, 5, 7})
            while (temp % i == 0)
                temp /= i;

        if (temp > 1)
            return "-1";

        int n = num.length();
        rem[0] = t, rem[n] = 0;
        int pos = n - 1;
        for (int i = 0; i < n; i++) {
            if (num[i] == '0') {
                pos = i;
                break;
            }
            long long digit = num[i] - '0';
            rem[i + 1] = rem[i] / GCD[digit][rem[i] % digit];
        }
        if (rem[n] == 1)
            return num;

        for (int i = pos; i >= 0; i--) {
            while (++num[i] <= '9') {
                long long digit = num[i] - '0';
                auto curr = rem[i] / GCD[digit][rem[i] % digit];
                int k = 9;
                for (int j = n - 1; j > i; j--) {
                    while (curr % k)
                        k--;

                    curr /= k;
                    num[j] = '0' + k;
                }
                if (curr == 1)
                    return num;
            }
        }

        int p = MAXN + 1;
        for (int i = 9; i > 1; i--) {
            while (t % i == 0) {
                buf[--p] = i + '0';
                t /= i;
            }
        }

        while (MAXN - p < n)
            buf[--p] = '1';

        return string(buf + p, MAXN + 1 - p);
    }
};