class Solution {
    public int numberOfSets(int n, int k) {
        long MOD = 1000000007L;
        long[][] dp = new long[k + 1][n];

        for (int i = 0; i < n; i++) {
            dp[0][i] = 1;
        }

        for (int seg = 1; seg <= k; seg++) {
            long sum = 0;

            for (int i = 1; i < n; i++) {
                sum = (sum + dp[seg - 1][i - 1]) % MOD;
                dp[seg][i] = (dp[seg][i - 1] + sum) % MOD;
            }
        }

        return (int) dp[k][n - 1];
    }
}