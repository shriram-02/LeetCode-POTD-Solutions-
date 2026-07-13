class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length):
                num = int(s[i:i + length])
                if low <= num <= high:
                    ans.append(num)

        return ans