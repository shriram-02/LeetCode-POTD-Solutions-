class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter

        CAP = k

        def comb_cap(n, r):
            r = min(r, n - r)
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) // i
                if res > CAP:
                    return CAP
            return res

        def count_perm(cnt):
            ways = 1
            rem = 0
            for c in cnt:
                if c:
                    ways *= comb_cap(rem + c, c)
                    if ways > CAP:
                        return CAP
                    rem += c
            return ways

        freq = Counter(s)
        half = [0] * 26
        mid = ""
        for ch, f in freq.items():
            half[ord(ch) - 97] = f // 2
            if f % 2:
                mid = ch

        if count_perm(half) < k:
            return ""

        left = []
        total = sum(half)

        for _ in range(total):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                ways = count_perm(half)
                if ways >= k:
                    left.append(chr(i + 97))
                    break
                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]