class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m
        if n == 2:
            return m * (m - 1) % MOD

        up = [0] * m
        down = [0] * m

        for i in range(m):
            up[i] = i
            down[i] = m - 1 - i

        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            new_up = [0] * m
            new_down = [0] * m

            for i in range(m):
                new_up[i] = pref_down[i]
                new_down[i] = (total_up - pref_up[i + 1]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD