# 최소 몇 번 이동 I = 300 -> BFS

import sys
from collections import deque

input_data = sys.stdin.readline

T = int(input_data())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0]*I for _ in range(I)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if nx == ax and ny == ay:
                    return visited[nx][ny] - 1
    return 0


for _ in range(T):
    I = int(input_data())
    board = [[0]*I for _ in range(I)]
    x, y = map(int, input_data().split())
    ax, ay = map(int, input_data().split())
    print(bfs(x, y))

