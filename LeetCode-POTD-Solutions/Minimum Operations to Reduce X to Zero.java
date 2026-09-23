class Solution {
    public int minOperations(int[] nums, int x) {
        int n = nums.length;
        long total = 0;
        
        for (int num : nums) {
            total += num;
        }
        
        long target = total - x;
        if (target < 0) return -1;
        if (target == 0) return n;
        
        int left = 0;
        long sum = 0;
        int maxLen = -1;
        
        for (int right = 0; right < n; right++) {
            sum += nums[right];
            
            while (left <= right && sum > target) {
                sum -= nums[left++];
            }
            
            if (sum == target) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }
        
        return maxLen == -1 ? -1 : n - maxLen;
    }
}