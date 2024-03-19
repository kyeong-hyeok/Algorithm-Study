# 겹치지 않기, 도형 연결, 정사각형 변끼리 연결 (꼭짓점끼리 x)

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
paper = [list(map(int, input_data().split())) for _ in range(N)]
ro = [[[1, 0], [1, 0], [1, 1]],
      [[1, 0], [1, 1], [0, 1]],
      [[1, 0], [1, 1], [1, 0]],
      [[0, 1], [0, 1], [1, 1]],
      [[0, 1], [1, 1], [1, 0]]]


def rotation(r):
    x, y = len(r), len(r[0])
    tmp = [[0]*x for _ in range(y)]
    for i in range(x):
        for j in range(y):
            tmp[j][i] = r[x-i-1][j]
    return tmp


for i in range(5):      # 도형 회전
    for j in range(3):
        if j == 0:
            ro.append(rotation(ro[i]))
        else:
            ro.append(rotation(ro[-1]))
ro.append([[1, 1, 1, 1]])   # ㅡ
ro.append([[1], [1], [1], [1]])     # ㅣ
ro.append([[1, 1], [1, 1]])     # ㅁ

result = 0
for i in range(N):  # O(250000) * O(138) = 약 O(30,000,000)
    for j in range(M):
        for k in range(len(ro)):
            if i <= N - len(ro[k]) and j <= M - len(ro[k][0]):
                r = 0
                for x in range(len(ro[k])):
                    for y in range(len(ro[k][0])):
                        r += paper[i+x][j+y]*ro[k][x][y]
                result = max(result, r)

print(result)