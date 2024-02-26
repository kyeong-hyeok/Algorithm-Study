# 빌딩 N = 50
# 선분 겹치는지 확인 -> 직선의 기울기로 확인
# 머릿속에 그림을 그려보고 기울기 비교 -> 어렵다면 직접 그림을 그려보기

# 헷갈렸던 부분
# 낮은 건물에서 높은 건물을 볼 수 있음!

import sys

input_data = sys.stdin.readline

N = int(input_data())
h = list(map(int, input_data().split()))


def check(a, b, c, d, e, f):
    if (d-b) / (c-a) <= (f-b) / (e-a):
        return 1
    return 0


result = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        p = 1
        if j < i:
            for k in range(j+1, i):
                if check(j, h[j], i, h[i], k, h[k]):
                    p = 0
                    break
        elif j > i:
            for k in range(i+1, j):
                if check(i, h[i], j, h[j], k, h[k]):
                    p = 0
                    break
        if p:
            cnt += 1
    result = max(result, cnt)

print(result)