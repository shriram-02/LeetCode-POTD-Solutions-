class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        ans = []

        for i in range(min(nums), max(nums) + 1):
            if i not in s:
                ans.append(i)

        return ans