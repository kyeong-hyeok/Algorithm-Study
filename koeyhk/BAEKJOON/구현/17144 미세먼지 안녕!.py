# 미세먼지 확산 (인접한 방향에 공기청정기 있으면 x)
# 값/5만큼 확산, 해당 지점 값은 값/5 * 확산 개수만큼 줄어듦
# 공기청정기 작동 - 위쪽 반시계, 아래쪽 시계
# 바람의 방향대로 미세먼지가 한 칸씩 이동 - 공기청정기로 들어가면 정화됨
# R, C = 50, T = 1,000

# 디버깅
# 주어진 조건을 만족하는지 차근차근 확인하기
# 공기청정기 순환 -> 인덱스 조심

import sys

input_data = sys.stdin.readline

R, C, T = map(int, input_data().split())
board = [list(map(int, input_data().split())) for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def rotation(ma):
    ua = ma - 1
    for i in range(ua - 2, -1, -1):
        board[i + 1][0] = board[i][0]
    for i in range(1, C):
        board[0][i - 1] = board[0][i]
    for i in range(1, ua + 1):
        board[i - 1][C - 1] = board[i][C - 1]
    for i in range(C - 1, 1, -1):
        board[ua][i] = board[ua][i - 1]
    board[ua][1] = 0
    for i in range(ma + 1, R - 1):
        board[i][0] = board[i + 1][0]
    for i in range(0, C - 1):
        board[R - 1][i] = board[R - 1][i + 1]
    for i in range(R - 1, ma, -1):
        board[i][C - 1] = board[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[ma][i] = board[ma][i - 1]
    board[ma][1] = 0


def spread():
    move = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] >= 5:
                d = board[x][y] // 5
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        move[nx][ny] += d
                        board[x][y] -= d
    for i in range(R):
        for j in range(C):
            board[i][j] += move[i][j]


def solution(board):
    for i in range(R):
        if board[i][0] == -1:
            ma = i + 1
            break
    for _ in range(T):
        spread()
        rotation(ma)
    result = 0
    board[ma][0], board[ma-1][0] = 0, 0
    for i in range(R):
        result += sum(board[i])
    print(result)


solution(board)