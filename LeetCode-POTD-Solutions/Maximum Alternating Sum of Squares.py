
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)
        squares = [x * x for x in nums]
        return sum(squares[len(nums) // 2:]) - sum(squares[:len(nums) // 2])
