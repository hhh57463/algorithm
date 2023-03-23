import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]

            if px < 0 or px >= N or py < 0 or py >= M:
                continue
            if graph[px][py] == 0:
                continue
            if graph[px][py] == 1:
                graph[px][py] = graph[x][y] + 1
                q.append((px, py))
                
    return graph[N-1][M-1]

print(bfs(0, 0))