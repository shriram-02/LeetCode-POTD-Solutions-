```python
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)

        # (left_char, right_char, prefix, suffix, best, length)
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            lc1, rc1, pre1, suf1, best1, len1 = a
            lc2, rc2, pre2, suf2, best2, len2 = b

            prefix = pre1
            suffix = suf2
            best = max(best1, best2)

            if rc1 == lc2:
                best = max(best, suf1 + pre2)

                if pre1 == len1:
                    prefix = len1 + pre2

                if suf2 == len2:
                    suffix = len2 + suf1

            return (
                lc1,
                rc2,
                prefix,
                suffix,
                best,
                len1 + len2
            )

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx):
            if l == r:
                tree[node] = (s[idx], s[idx], 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx)
            else:
                update(node * 2 + 1, mid + 1, r, idx)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            s[idx] = ch
            update(1, 0, n - 1, idx)
            ans.append(tree[1][4])

        return ans
```
