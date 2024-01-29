# M, N = 100

# 디버깅에서 수정한 것
# bfs 함수에서 board[nx][ny] 대신 board[i][j]를 사용!

import sys
from collections import deque
input_data = sys.stdin.readline

M, N, K = map(int, input_data().split())
board = [[0]*N for _ in range(M)]
for _ in range(K):
    b, a, d, c = map(int, input_data().split())     # 0 2 4 4
    a = M-a     # 2 -> 3
    c = M-c     # 4 -> 1
    for i in range(c, a):   # 1 3
        for j in range(b, d):   # 0 4
            board[i][j] = 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    board[x][y] = 1
    result = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                board[nx][ny] = 1
                result += 1
                q.append((nx, ny))
    return result


answer = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))