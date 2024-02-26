# N = 1,000
# 지붕 오목한 부분 X, 수평 부분은 어떤 기둥의 윗면과 닿아야 함

# 처음 풀이
# 높이 최댓값 이전: i를 늘려가며 기둥의 높이와 비교하고 면적 더하기
# 높이 최댓값 이후: 맨 뒤부터 i를 감소하며 기둥의 높이와 비교하고 면적 더하기

# 인덱스 조건을 실수하지 않아야 하기 때문에 구현하기 어려운 방법

import sys

input_data = sys.stdin.readline

N = int(input_data())
col = [list(map(int, input_data().split())) for _ in range(N)]
col.sort()
max_l = 0
for i in range(N):
    max_l = max(max_l, col[i][1])
if N == 1:
    print(col[0][1])
    exit()
i, j, l, result = col[0][0], 1, col[0][1], 0

while i <= col[-1][0]:
    if i < col[j][0]:
        result += l
    else:
        if l < col[j][1]:
            l = col[j][1]
        result += l
        j += 1
        if max_l == l:
            break
    i += 1


r = col[-1][0] + 1
j = len(col) - 2
l = col[-1][1]
while r > i + 1:
    if r > col[j][0] + 1:
        result += l
    else:
        if l < col[j][1]:
            l = col[j][1]
        result += l
        j -= 1
    r -= 1


print(result)


# 개선한 풀이
# 최대 높이를 기준으로 좌우로 나누어 최댓값을 갱신하면서 더하기

import sys

input_data = sys.stdin.readline

N = int(input_data())
col = [0] * 1001
max_l = 0
for _ in range(N):
    L, H = map(int, input_data().split())
    col[L] = H
    if H > max_l:
        max_l = H
        inx = L

result = 0
cur = 0
for i in range(inx+1):
    cur = max(cur, col[i])
    result += cur
cur = 0
for i in range(1000, inx, -1):
    cur = max(cur, col[i])
    result += cur
print(result)