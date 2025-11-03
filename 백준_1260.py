import sys                    # 빠른 입력을 위해 sys 모듈 사용
from collections import deque  # BFS에 사용할 큐 자료구조

input = sys.stdin.readline     # 입력 속도 향상
sys.setrecursionlimit(10**6)   # DFS 재귀 깊이 한도를 넉넉히 올림

# N: 정점 수, M: 간선 수, V: 시작 정점
N, M, V = map(int, input().split())

# 인접 리스트 초기화 (정점 번호가 1부터라서 N+1 크기)
adj = [[] for _ in range(N + 1)]

# 간선 입력 (양방향)
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)           # a -> b
    adj[b].append(a)           # b -> a (양방향)

# 방문 우선순위: 번호가 작은 정점부터 방문해야 하므로 정렬
for i in range(1, N + 1):
    adj[i].sort()

# -------------------- DFS --------------------
visited = [False] * (N + 1)    # 방문 여부 배열
dfs_order = []                 # DFS 방문 순서를 담을 리스트

def dfs(u: int) -> None:       # 현재 정점 u에서 DFS 수행
    visited[u] = True          # u 방문 체크
    dfs_order.append(u)        # 방문 순서에 u 추가
    for v in adj[u]:           # u와 인접한 정점들을 작은 번호부터 확인
        if not visited[v]:     # 아직 방문하지 않았다면
            dfs(v)             # 재귀 호출로 계속 탐색

dfs(V)                         # 시작 정점 V에서 DFS 시작

# -------------------- BFS --------------------
visited = [False] * (N + 1)    # DFS에서 쓴 visited를 초기화
bfs_order = []                 # BFS 방문 순서를 담을 리스트
q = deque([V])                 # 큐 초기화: 시작 정점 V를 넣고 시작
visited[V] = True              # 큐에 넣을 때 바로 방문 체크(중복 삽입 방지)

while q:                       # 큐가 빌 때까지 반복
    u = q.popleft()            # 큐의 앞에서 하나 꺼냄
    bfs_order.append(u)        # 방문 순서에 u 추가
    for v in adj[u]:           # u의 인접 정점들을 작은 번호부터 확인
        if not visited[v]:     # 아직 방문하지 않았다면
            visited[v] = True  # 큐에 넣는 순간 방문 체크
            q.append(v)        # 다음 레벨 탐색을 위해 큐에 삽입

# 결과 출력: 문제 요구대로 공백으로 구분해 방문 순서 출력
print(*dfs_order)
print(*bfs_order)

