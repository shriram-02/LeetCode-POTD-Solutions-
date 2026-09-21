class Solution {
    public long[] resultArray(int[] nums, int k) {
        long[] result = new long[k];
        long[] dp = new long[k];

        for (int num : nums) {
            long[] next = new long[k];

            int val = num % k;
            next[val]++;

            for (int r = 0; r < k; r++) {
                if (dp[r] > 0) {
                    next[(int)((long) r * val % k)] += dp[r];
                }
            }

            for (int r = 0; r < k; r++) {
                result[r] += next[r];
            }

            dp = next;
        }

        return result;
    }
}