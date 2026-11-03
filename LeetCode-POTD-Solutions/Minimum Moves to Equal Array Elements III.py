class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(max(nums) - num for num in nums)