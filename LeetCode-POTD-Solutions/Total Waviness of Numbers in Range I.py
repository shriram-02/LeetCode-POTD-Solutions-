class Solution(object):
    def totalWaviness(self, num1, num2):
        def waviness(x):
            s = str(x)
            n = len(s)
            if n < 3:
                return 0
            
            cnt = 0
            for i in range(1, n - 1):
                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or \
                   (s[i] < s[i - 1] and s[i] < s[i + 1]):
                    cnt += 1
            return cnt
        
        ans = 0
        for x in range(num1, num2 + 1):
            ans += waviness(x)
        return ans