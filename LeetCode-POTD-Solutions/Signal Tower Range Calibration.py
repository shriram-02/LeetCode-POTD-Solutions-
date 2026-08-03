# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
th = list(map(int, input().split()))

low = max(th)
high = low + (max(x) - min(x))

def check(p):
    left = -10**20
    right = 10**20

    for xi, t in zip(x, th):
        if p < t:
            return False
        d = p - t
        left = max(left, xi - d)
        right = min(right, xi + d)
        if left > right:
            return False
    return True

while low < high:
    mid = (low + high) // 2
    if check(mid):
        high = mid
    else:
        low = mid + 1

print(low)