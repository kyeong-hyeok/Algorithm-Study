# N = 100
# O(N^4)까지 가능

# 풀이 아이디어
# ㅣ와 ㅡ, 그리고 ㅁ는 따로 처리하고, 다른 블록은 2*3 배열로 묶어서 회전해 처리
# 인덱스에 주의해야 함!

import sys
input_data = sys.stdin.readline

block = [[[1, 1, 0], [0, 1, 1]], [[1, 1, 1], [0, 0, 1]], [[1, 1, 1], [0, 1, 0]], [[1, 1], [1, 1]]]


def rotation(block):
    n = len(block)  # 2
    m = len(block[0])  # 3
    tmp = [[0]*n for _ in range(m)]
    for j in range(m):  # 3
        for i in range(n):  # 2
            tmp[j][i] = block[n-i-1][j]
    return tmp


p = 1
while 1:
    result = -10e9
    N = int(input_data())
    if N == 0:
        break
    board = [list(map(int, input_data().split())) for _ in range(N)]
    for i in range(N):      # O(N^2) * O(4*3*6)
        for j in range(N):
            for k in range(3):      # 블록에 돌아가는 for 문
                for _ in range(4):      # 90도 방향을 회전 4번 수행
                    block[k] = rotation(block[k])
                    if len(block[k][0]) + j <= N and len(block[k]) + i <= N:    # 범위 확인
                        r = 0
                        for x in range(len(block[k])):
                            for y in range(len(block[k][0])):
                                r += block[k][x][y] * board[i+x][j+y]
                        result = max(result, r)
                if i < N-1 and j < N-1:     # 정사각형 블록
                    result = max(result, board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1])
                if j <= N-4:    # ㅡ 블록
                    result = max(result, board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3])
                if i <= N-4:    # ㅣ 블록
                    result = max(result, board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j])
    print(str(p)+'. ' + str(result))
    p += 1
