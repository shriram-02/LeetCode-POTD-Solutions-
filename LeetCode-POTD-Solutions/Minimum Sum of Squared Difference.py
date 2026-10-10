class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            if sum(max(0, d - mid) for d in diff) <= k:
                right = mid
            else:
                left = mid + 1

        diff = [min(d, left) for d in diff]
        remaining = k - sum(max(0, d - left) for d in [abs(a - b) for a, b in zip(nums1, nums2)])

        for i in range(len(diff)):
            if remaining > 0 and diff[i] == left:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)