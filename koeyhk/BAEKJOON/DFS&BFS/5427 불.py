# T = 100, w h = 1,000
# . 빈공간, # 벽, @ 시작 위치, * 불

# BFS O(T*wh)
# 불 먼저 이동 -> 상근이 이동

import sys
from collections import deque

input_data = sys.stdin.readline


def bfs():
    while q:
        x, y, k = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '#':
                if k == 1 and board[nx][ny] != '*':
                    board[nx][ny] = '*'
                    q.append((nx, ny, 1))
                elif k == 0 and board[nx][ny] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny, 0))
                    if nx == 0 or nx == h-1 or ny == 0 or ny == w-1:
                        return visited[nx][ny]
    return -1


T = int(input_data())
for _ in range(T):
    w, h = map(int, input_data().split())
    board = [list(input_data().rstrip()) for _ in range(h)]
    if w == 1 and h == 1:
        print(1)
        continue
    q = deque()
    x, y = -1, -1
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                q.append((i, j, 1))
            elif board[i][j] == '@':
                x, y = i, j
                visited[x][y] = 1
    if x == 0 or x == h-1 or y == 0 or y == w-1:
        print(1)
        continue
    q.append((x, y, 0))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    result = bfs()
    if result == -1:
        print('IMPOSSIBLE')
    else:
        print(result)