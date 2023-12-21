# 모눈종이의 크기 = 스티커의 크기에 꼭 맞음 -> 범위 벗어나는지 확인하기 위해 필요한 조건
# 위 (1순위) -> 왼쪽 (2순위) 위치로 스티커 붙이기
# 스티커를 붙일 수 있는 위치 x -> 시계 방향으로 90도 회전해 붙일 자리 탐색
# 4번 회전(0, 90, 180, 270)시켰을 때 붙이지 못하면 버림
# N=40, M=40, K=100 -> 완전탐색으로 가능

# 필요한 메서드
# 스티커를 붙일 공간이 있는지 확인하는 메서드 - isMatch
# 스티커를 회전하는 메서드 - rotation

# 추가한 메서드
# 스티커를 모눈종이에 붙이는 메서드 -> 가독성 향상

import sys

input_data = sys.stdin.readline

N, M, K = map(int, input_data().split())
R = []
C = []
sticker = []
for i in range(K):
    r, c = map(int, input_data().split())
    R.append(r)
    C.append(c)
    s = []
    for j in range(r):
        s.append(list(map(int, input_data().split())))
    sticker.append(s)

paper = [[0] * M for _ in range(N)]


def isMatch(st, paper):     # 스티커를 붙일 공간이 있는지 확인
    width = len(st[0])
    height = len(st)
    for i in range(N-height+1):
        for j in range(M-width+1):
            x, y = 0, 0
            while 1:
                if st[x][y] + paper[i+x][j+y] == 2:
                    break
                y += 1
                if y == width:
                    y, x = 0, x+1
                if x == height:
                    return i, j
    return -1, -1


def rotation(st):       # 스티커를 시계 방향으로 90도 회전
    width = len(st[0])
    height = len(st)
    rst = [[0] * height for _ in range(width)]
    for i in range(width):
        for j in range(height):
            rst[i][j] = st[height-j-1][i]
    return rst


def attach(st, paper):      # 스티커 붙이기
    width = len(st[0])
    height = len(st)
    x, y = 0, 0
    while 1:
        if st[x][y] == 1:
            paper[a + x][b + y] = 1
        y += 1
        if y == width:
            y, x = 0, x + 1
        if x == height:
            return


for st in sticker:
    for i in range(4):
        a, b = isMatch(st, paper)
        if a != -1 and b != -1:     # 스티커 붙일 공간이 있다면 -> 붙이기
            attach(st, paper)
            break
        st = rotation(st)

result = 0
for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            result += 1

print(result)