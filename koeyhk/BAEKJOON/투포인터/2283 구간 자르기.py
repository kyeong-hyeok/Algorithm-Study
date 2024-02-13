# N = 1,000 -> O(N^2)까지
# 이분탐색 ? 투포인터 ?

# 누적합 + 투포인터 풀이

import sys
sys.setrecursionlimit(10**8)

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
line = [0] * 1000001
max_l = 0
for _ in range(N):
    a, b = map(int, input_data().split())
    max_l = max(max_l, b)
    for i in range(a, b):       # 시간 초과 최악 -> O(1,000,000,000) * O(N)
        line[i] += 1

l, r, result = 0, 0, 0
while l <= r <= max_l:      # O(N)
    if result < K:
        result += line[r]
        r += 1
    elif result > K:
        result -= line[l]
        l += 1
    else:
        print(l, r)
        exit()

print(0, 0)


# 처음 풀이
# N = 1,000 -> O(N^2)까지
# 투포인터 풀이

import sys
sys.setrecursionlimit(10**8)

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
line = [list(map(int, input_data().split())) for _ in range(N)]
max_l = 0
for i in range(N):
    max_l = max(max_l, line[i][1])
answer = 0
d = dict()


def check(x, y):    # O(N)
    result = 0
    for i in range(N):
        if y >= line[i][0] >= x and x <= line[i][1] <= y:
            result += line[i][1] - line[i][0]
        elif line[i][0] <= x and x <= line[i][1] <= y:
            result += line[i][1] - x
        elif y >= line[i][0] >= x and line[i][1] >= y:
            result += y - line[i][0]
        elif line[i][0] <= x and line[i][1] >= y:
            result += y - x
    return result


l, r = 0, 0
while l <= r <= max_l:  # 최악 O(N^3)
    t = check(l, r)
    if t < K:
        r += 1
    elif t > K:
        l += 1
    else:
        print(l, r)
        exit()

print(0, 0)
