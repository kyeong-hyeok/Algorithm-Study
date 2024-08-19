# 주사위 굴림
# 이동한 칸의 수가 0이면, 주사위 바닥면의 수가 복사됨
# 이동한 칸의 수가 0이 아니면, 칸의 수가 주사위 바닥면으로 복사됨, 칸의 수는 0이 됨

import sys
from collections import deque
input_data = sys.stdin.readline


def mov(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < N and 0 <= ny < M:
        if d == 1:      # 동
            a.rotate(1)
            b[1] = a[1]
            tmp = a[0]
            a[0] = b[3]
            b[3] = tmp
        elif d == 2:           # 서
            a.rotate(-1)
            b[1] = a[1]
            tmp = a[2]
            a[2] = b[3]
            b[3] = tmp
        elif d == 3:            # 북
            b.rotate(-1)
            a[1] = b[1]
        elif d == 4:            # 남
            b.rotate(1)
            a[1] = b[1]
        if m[nx][ny] == 0:
            m[nx][ny] = b[3]
        else:
            b[3] = m[nx][ny]
            m[nx][ny] = 0
        print(b[1])
        return nx, ny
    return x, y


N, M, x, y, K = map(int, input_data().split())
m = [list(map(int, input_data().split())) for _ in range(N)]
a = deque([0, 0, 0])    # 주사위 가로
b = deque([0, 0, 0, 0])     # 주사위 세로
move = list(map(int, input_data().split()))
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for d in move:
    x, y = mov(x, y, d)