class Solution {
public:
    int countCommas(int n) {
        int ans = 0;

        if (n >= 1000)
            ans += n - 999;

        if (n >= 1000000)
            ans += n - 999999;

        return ans;
    }
};