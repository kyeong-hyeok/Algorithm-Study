# 2 <= M, N <= 1000 -> 완전 탐색 10^6
# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토가 익게 됨
# 익은 토마토에서 BFS 시작

# 중요한 부분
# 1. 익은 토마토들을 먼저 큐에 삽입한 후 BFS 수행

import sys
from collections import deque

input_data = sys.stdin.readline

M, N = map(int, input_data().split())
box = [list(map(int, input_data().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                box[nx][ny] = 1
                q.append((nx, ny))
    result = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
            result = max(result, visited[i][j])
    return result - 1


print(bfs())