import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))

adj = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

subtree = [0] * n
resonance = [0] * n
total_devotion = sum(values)

# First DFS: compute subtree sums and resonance for root (node 0)
def dfs1(u, p, dist):
    subtree[u] = values[u]
    resonance[0] += values[u] * dist
    for v, w in adj[u]:
        if v == p:
            continue
        dfs1(v, u, dist + w)
        subtree[u] += subtree[v]

# Second DFS: rerooting to compute resonance for all nodes
def dfs2(u, p):
    for v, w in adj[u]:
        if v == p:
            continue
        resonance[v] = resonance[u] + (total_devotion - 2 * subtree[v]) * w
        dfs2(v, u)

dfs1(0, -1, 0)
dfs2(0, -1)

print(" ".join(map(str, resonance)))
