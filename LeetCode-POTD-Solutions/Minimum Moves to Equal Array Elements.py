class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)