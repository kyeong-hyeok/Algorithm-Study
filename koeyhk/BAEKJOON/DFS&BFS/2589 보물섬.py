import sys
from collections import deque

input_data = sys.stdin.readline
N, M = map(int, input_data().split())
t = []
for i in range(N):
    t.append(list(input_data().rstrip()))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and t[nx][ny] == 'L' and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited[x][y] - 1


result = 0
for i in range(N):
    for j in range(M):
        if t[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)