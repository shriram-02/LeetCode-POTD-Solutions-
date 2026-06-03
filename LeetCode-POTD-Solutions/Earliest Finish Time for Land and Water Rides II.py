from bisect import bisect_right

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def build(start, dur):
            rides = sorted(zip(start, dur))
            s = [x for x, _ in rides]
            n = len(rides)

            pref = [0] * n
            pref[0] = rides[0][1]
            for i in range(1, n):
                pref[i] = min(pref[i - 1], rides[i][1])

            suff = [0] * n
            suff[-1] = rides[-1][0] + rides[-1][1]
            for i in range(n - 2, -1, -1):
                suff[i] = min(suff[i + 1], rides[i][0] + rides[i][1])

            return s, pref, suff

        wS, wPref, wSuff = build(waterStartTime, waterDuration)
        lS, lPref, lSuff = build(landStartTime, landDuration)

        INF = float('inf')
        ans = INF

        for s, d in zip(landStartTime, landDuration):
            a = s + d
            idx = bisect_right(wS, a)

            cur = INF
            if idx > 0:
                cur = min(cur, a + wPref[idx - 1])
            if idx < len(wS):
                cur = min(cur, wSuff[idx])

            ans = min(ans, cur)

        for s, d in zip(waterStartTime, waterDuration):
            b = s + d
            idx = bisect_right(lS, b)

            cur = INF
            if idx > 0:
                cur = min(cur, b + lPref[idx - 1])
            if idx < len(lS):
                cur = min(cur, lSuff[idx])

            ans = min(ans, cur)

        return ans