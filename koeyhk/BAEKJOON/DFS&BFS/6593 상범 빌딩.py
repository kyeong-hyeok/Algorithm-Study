# L, R, C = 30
# 금 #, 빈 칸 ., 시작 S, 출구 E

# BFS + 구현 문제
# 인덱스가 벗어나지 않도록 좌표 설정 후 구현

import sys
from collections import deque
input_data = sys.stdin.readline

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(x, y, z):
    q = deque()
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited[x][y][z] = 1
    q.append((x, y, z))
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C and b[nx][ny][nz] != '#' and visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append((nx, ny, nz))
                if b[nx][ny][nz] == 'E':
                    return visited[nx][ny][nz] - 1
    return -1


while 1:
    L, R, C = map(int, input_data().split())
    if L == 0 and R == 0 and C == 0:
        break
    b = []
    for i in range(L):
        b.append([list(input_data().rstrip()) for _ in range(R)])
        input_data()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if b[i][j][k] == 'S':
                    result = bfs(i, j, k)
                    break
    if result == -1:
        print("Trapped!")
    else:
        print(f'Escaped in {result} minute(s).')