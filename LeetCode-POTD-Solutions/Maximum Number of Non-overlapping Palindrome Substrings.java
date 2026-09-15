class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int[] best = new int[n + 1];

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) &&
                    (j - i < 2 || dp[i + 1][j - 1])) {
                    dp[i][j] = true;
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            best[i] = best[i - 1];

            for (int start = 0; start < i; start++) {
                if (i - start >= k && dp[start][i - 1]) {
                    best[i] = Math.max(best[i], best[start] + 1);
                }
            }
        }

        return best[n];
    }
}