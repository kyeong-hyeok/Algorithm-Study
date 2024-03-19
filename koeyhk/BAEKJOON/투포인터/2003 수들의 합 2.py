# N = 10,000 M = 300,000,000, A[X] <= 30,000 자연수
# 문제 제한 0.5초 < O(N^2) 1초

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))

cnt = 0
s, e = 0, 0
result = num[s]
while 1:
    if result >= M:
        if result == M:
            cnt += 1
        result -= num[s]
        s += 1
    else:
        e += 1
        if e >= N:
            break
        result += num[e]

print(cnt)