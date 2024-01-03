# 35분
# R, C 1000 -> BFS O(1,000,000)
# BFS 큐에 불 추가 후 지훈이 추가 (지훈이를 먼저 추가하면 불길에 휩싸일 수 있기 때문)

# 놓친 부분
# 1. 지훈이가 처음부터 미로의 가장자리에 접해 있을 경우 -> 바로 탈출 가능

import sys
from collections import deque
input_data = sys.stdin.readline

R, C = map(int, input_data().split())
miro = [list(input_data().rstrip()) for _ in range(R)]
fire = []
for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            jx, jy = i, j
            miro[i][j] = '.'
        elif miro[i][j] == 'F':
            fire.append((i, j))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

if jx == 0 or jx == R-1 or jy == 0 or jy == C-1:
    print(1)
    exit()


def bfs():
    q = deque()
    visited = [[0]*C for _ in range(R)]
    for f in fire:
        q.append((f[0], f[1], 0))
        visited[f[0]][f[1]] = -1
    q.append((jx, jy, 1))
    visited[jx][jy] = 1
    while q:
        x, y, k = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if k != 0:      # 지훈이
                if 0 <= nx < R and 0 <= ny < C and miro[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, k+1))
                    if nx == 0 or nx == R-1 or ny == 0 or ny == C-1:
                        return k+1
            else:           # 불
                if 0 <= nx < R and 0 <= ny < C and miro[nx][ny] != '#' and visited[nx][ny] != -1:
                    visited[nx][ny] = -1
                    q.append((nx, ny, 0))
    return -1


result = bfs()
if result == -1:
    print('IMPOSSIBLE')
else:
    print(result)