class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        r = 1

        for x in sorted(set(arr)):
            rank[x] = r
            r += 1

        return [rank[x] for x in arr]