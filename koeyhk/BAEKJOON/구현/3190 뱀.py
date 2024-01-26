# 사과 먹으면 길이 + 1, 벽 또는 자신의 몸과 부딪히면 게임 끝
# N = 100 -> O(N^2) 구현

# 디버깅!
# 15 D -> 이렇게 입력될 때 list(input().split())으로 받아 ['1','5',' ','D','\n'] 이렇게 저장됨
# **잘못된 부분 예제로 판단하고 디버깅하기**

import sys
from collections import deque
input_data = sys.stdin.readline

N = int(input_data())
K = int(input_data())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input_data().split())
    board[x-1][y-1] = 1
L = int(input_data())
dir = []
for _ in range(L):
    a, b = input_data().split()
    dir.append((int(a), b))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y, k, t, d = 0, 0, 0, 0, 1
board[0][0] = -1
q = deque([(0, 0)])     # 몸의 위치를 저장하는 큐
while 1:
    x += dx[d]
    y += dy[d]
    t += 1
    if x < 0 or x >= N or y < 0 or y >= N or board[x][y] == -1:
        break
    if board[x][y] != 1:        # 이동한 칸에 사과가 없다면 몸에서 처음 위치 꺼내기
        a, b = q.popleft()
        board[a][b] = 0
    board[x][y] = -1        # 현재 머리 위치 저장
    q.append((x, y))
    if k < L and dir[k][0] == t:
        if dir[k][1] == 'L':
            d = (d+3) % 4
        else:
            d = (d+1) % 4
        k += 1

print(t)