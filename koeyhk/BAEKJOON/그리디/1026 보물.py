# 음수인 정수가 없으므로 A의 최솟값과 B의 최댓값을 곱하면 된다!

import sys

input_data = sys.stdin.readline
N = int(input_data())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
S = 0
for i in range(N):
    num = max(B)
    S += A[i] * num
    del B[B.index(num)]

print(S)