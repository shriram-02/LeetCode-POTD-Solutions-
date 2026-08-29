from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((x, i) for i, x in enumerate(nums))
        ans = nums[:]

        i = 0
        while i < n:
            j = i
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j + 1))
            values = sorted(arr[k][0] for k in range(i, j + 1))

            for idx, val in zip(indices, values):
                ans[idx] = val

            i = j + 1

        return ans