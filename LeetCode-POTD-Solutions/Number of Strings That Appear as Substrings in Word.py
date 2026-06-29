class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0

        for p in patterns:
            if p in word:
                count += 1

        return count