import math

class Solution:
    def RangeLCMQuery(self, arr, queries):
        
        def lcm(a, b):
            return (a * b) // math.gcd(a, b)
        
        n = len(arr)
        seg = [1] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                seg[node] = arr[start]
                return
            
            mid = (start + end) // 2
            
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            
            seg[node] = lcm(seg[2 * node], seg[2 * node + 1])
        
        def update(node, start, end, idx, val):
            if start == end:
                seg[node] = val
                return
            
            mid = (start + end) // 2
            
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            
            seg[node] = lcm(seg[2 * node], seg[2 * node + 1])
        
        def query(node, start, end, l, r):
            if r < start or end < l:
                return 1
            
            if l <= start and end <= r:
                return seg[node]
            
            mid = (start + end) // 2
            
            left = query(2 * node, start, mid, l, r)
            right = query(2 * node + 1, mid + 1, end, l, r)
            
            return lcm(left, right)
        
        build(1, 0, n - 1)
        
        res = []
        
        for q in queries:
            if q[0] == 1:
                _, idx, val = q
                arr[idx] = val
                update(1, 0, n - 1, idx, val)
            else:
                _, l, r = q
                res.append(query(1, 0, n - 1, l, r))
        
        return res