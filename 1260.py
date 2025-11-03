import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 정점 번호가 작은 것부터 방문하도록 인접 리스트 정렬
for i in range(1, N + 1):
    adj[i].sort()

# DFS (재귀)
visited = [False] * (N + 1)
dfs_order = []

def dfs(u):
    visited[u] = True
    dfs_order.append(u)
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

dfs(V)

# BFS
visited = [False] * (N + 1)
bfs_order = []
q = deque([V])
visited[V] = True

while q:
    u = q.popleft()
    bfs_order.append(u)
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)

print(*dfs_order)
print(*bfs_order)
