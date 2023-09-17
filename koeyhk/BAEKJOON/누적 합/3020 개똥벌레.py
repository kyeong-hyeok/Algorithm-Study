import sys

input_data = sys.stdin.readline

N, H = map(int, input_data().split())
up, down = [0] * (H+1), [0] * (H+1)
for i in range(N):
    height = int(input_data())
    if i % 2 == 0:
        up[height] += 1
    else:
        down[height] += 1

for i in range(H-1, 0, -1):     # 누적 합 계산
    down[i] += down[i+1]
    up[i] += up[i+1]

result = N
min_count = 0

for i in range(1, H+1):
    cut = down[i] + up[H-i+1]
    if cut < result:    # 더 적게 파괴되는 경우
        result = cut
        min_count = 1
    elif cut == result:     # 해당 구간이 이미 있는 경우
        min_count += 1

print(result, min_count)


# 이전 풀이 - 시간 초과

import sys

input_data = sys.stdin.readline

N, H = map(int, input_data().split())
up = []
down = []
for i in range(N):
    if i % 2 == 0:
        up.append(int(input_data()))
    else:
        down.append(int(input_data()))

result = 2000000
i_count = 0
for i in range(H):
    count = 0
    for j in range(len(up)):    # N이 200,000일 때 최대 반복 횟수 500,000 * 200,000
        if i+0.5 <= up[j]:
            count += 1
        if i+0.5 >= H - down[j]:
            count += 1
    if count == result:
        i_count += 1
    elif count < result:
        i_count = 1
        result = count

print(result, i_count)