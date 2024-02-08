# 적록색약 -> R, G 같이 B 따로
# N = 100
# BFS -> O(N^2)

import sys
from collections import deque
input_data = sys.stdin.readline

N = int(input_data())
picture = [list(input_data().rstrip()) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, colors):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and picture[nx][ny] in colors:
                visited[nx][ny] = 1
                q.append((nx, ny))


visited = [[0] * N for _ in range(N)]
normal = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j, [picture[i][j]])
            normal += 1

visited = [[0] * N for _ in range(N)]
result = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            if picture[i][j] == 'R' or picture[i][j] == 'G':
                bfs(i, j, ['R', 'G'])
            else:
                bfs(i, j, ['B'])
            result += 1

print(normal, result)