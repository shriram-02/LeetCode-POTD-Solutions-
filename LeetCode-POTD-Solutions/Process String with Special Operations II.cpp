class Solution {
public:
    char processStr(string s, long long k) {
        int n = s.size();
        const long long LIM = (long long)1e15 + 5;

        vector<long long> len(n + 1, 0);

        for (int i = 0; i < n; i++) {
            long long cur = len[i];

            if (s[i] >= 'a' && s[i] <= 'z') {
                len[i + 1] = min(LIM, cur + 1);
            } else if (s[i] == '*') {
                len[i + 1] = (cur > 0 ? cur - 1 : 0);
            } else if (s[i] == '#') {
                len[i + 1] = min(LIM, cur * 2);
            } else { // '%'
                len[i + 1] = cur;
            }
        }

        if (k >= len[n]) return '.';

        for (int i = n - 1; i >= 0; i--) {
            long long before = len[i];
            char op = s[i];

            if (op >= 'a' && op <= 'z') {
                if (k == before) return op;
            } else if (op == '#') {
                if (before > 0 && k >= before) k -= before;
            } else if (op == '%') {
                if (before > 0) k = before - 1 - k;
            }
        }

        return '.';
    }
};