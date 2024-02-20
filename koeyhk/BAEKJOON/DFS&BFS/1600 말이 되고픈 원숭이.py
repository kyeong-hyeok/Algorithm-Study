# K번만 말처럼 움직일 수 있음. 왼쪽 위부터 오른쪽 아래까지
# 0 평지, 1 장애물

# 해당 칸에 도착했을 때 최솟값을 갱신하는 방법에 대해서 고민함 (K값 처리 방법)
# -> K값별로 visited를 설정해 해결
# 각각의 경로에 대해 영향을 받지 않고 최솟값을 구할 수 있음

import sys
from collections import deque

input_data = sys.stdin.readline

K = int(input_data())
W, H = map(int, input_data().split())
board = [list(map(int, input_data().split())) for _ in range(H)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
hx = [-2, -1, 1, 2, 2, 1, -1, -2]
hy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y, t):
    q = deque()
    visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]
    q.append((x, y, t, 0))
    visited[x][y][0] = 1
    result = W*H
    while q:
        x, y, t, cnt = q.popleft()
        if x == H - 1 and y == W - 1:
            return cnt
        if t < K:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and visited[nx][ny][t+1] == 0:
                    visited[nx][ny][t+1] = 1
                    q.append((nx, ny, t+1, cnt+1))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and visited[nx][ny][t] == 0:
                visited[nx][ny][t] = 1
                q.append((nx, ny, t, cnt+1))
    return -1


print(bfs(0, 0, 0))
