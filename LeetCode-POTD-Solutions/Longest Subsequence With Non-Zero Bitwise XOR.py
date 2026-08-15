class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        if x != 0:
            return len(nums)
        for num in nums:
            if num != 0:
                return len(nums) - 1
        return 0