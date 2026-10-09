
class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        need = 0

        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    res += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need < 0:
                    res += 1
                    need = 1

        return res + need
