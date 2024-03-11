# 0 = 빈칸, 1 = 벽, 2 = 바이러스
# N = 50, M = 10

# 놓친 부분
# 바이러스를 놓을 수 있는 칸 중에 M개를 선택해야 함
# visited = -1인 지점을 확인할 때 board에서 벽(1)이 아닌걸로 판단! (0 x)

import sys
from collections import deque
from itertools import combinations
input_data = sys.stdin.readline

N, M = map(int, input_data().split())
board = [list(map(int, input_data().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

comb = list(combinations(virus, M))
result = 100000000
for c in comb:
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    for i in c:
        q.append(i)
        visited[i[0]][i[1]] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1 and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    p = 1
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] != 1:
                p = 0
    if p:
        r = 0
        for i in range(N):
            r = max(r, max(visited[i]))
        result = min(result, r)

if result == 100000000:
    print(-1)
else:
    print(result)