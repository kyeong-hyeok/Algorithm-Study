import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input_data().strip())))

visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if nx == N-1 and ny == M-1:
                    return visited[nx][ny]


print(bfs(0, 0))
