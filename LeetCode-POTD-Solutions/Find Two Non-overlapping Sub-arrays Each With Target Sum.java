class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int[] best = new int[n];
        int INF = Integer.MAX_VALUE / 2;

        for (int i = 0; i < n; i++) {
            best[i] = INF;
        }

        int left = 0, sum = 0, minLen = INF, ans = INF;

        for (int right = 0; right < n; right++) {
            sum += arr[right];

            while (sum > target) {
                sum -= arr[left++];
            }

            if (sum == target) {
                int len = right - left + 1;

                if (left > 0 && best[left - 1] != INF) {
                    ans = Math.min(ans, best[left - 1] + len);
                }

                minLen = Math.min(minLen, len);
            }

            best[right] = minLen;
        }

        return ans == INF ? -1 : ans;
    }
}