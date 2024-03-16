# R, C = 5 K = 25

# 개선한 부분
# visited를 따로 만들지 않고 board[nx][ny]의 값을 변경시켜도 가능

import sys

input_data = sys.stdin.readline

R, C, K = map(int, input_data().split())
board = [list(input_data().rstrip()) for _ in range(R)]
result = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bt(x, y, cnt):
    global result
    if x == 0 and y == C-1:
        if cnt == K-1:
            result += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != 'T':
            board[nx][ny] = 'T'
            bt(nx, ny, cnt + 1)
            board[nx][ny] = '.'


board[R-1][0] = 'T'
bt(R - 1, 0, 0)
print(result)
