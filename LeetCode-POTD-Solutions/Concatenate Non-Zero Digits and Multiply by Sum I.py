class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        s = 0

        for d in str(n):
            if d != '0':
                x = x * 10 + int(d)
                s += int(d)

        return x * s