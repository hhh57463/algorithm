# https://ji-gwang.tistory.com/291 참고...
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs_v = [False] * (N + 1)
bfs_v = [False] * (N + 1)

def dfs(V):
    dfs_v[V] = True
    print(V, end=" ")
    for i in range(1, N + 1):
        if not dfs_v[i] and graph[V][i]:
            dfs(i)

def bfs(V):
    q = deque([V])
    bfs_v[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if not bfs_v[i] and graph[V][i]:
                q.append(i)
                bfs_v[i] = True

dfs(V)
print()
bfs(V)