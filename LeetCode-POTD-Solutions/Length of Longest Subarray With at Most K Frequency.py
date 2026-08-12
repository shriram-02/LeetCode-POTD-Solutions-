class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans