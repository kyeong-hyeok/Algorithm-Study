# 전형적인 BFS 문제
# 방문 여부 리스트를 통해 최단 거리 구하기

import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
maze = [list(map(int, input_data().rstrip())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if nx == N-1 and ny == M-1:
                    return visited[nx][ny]


print(bfs(0, 0))