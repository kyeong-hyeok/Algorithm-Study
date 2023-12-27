# 동전 간에 배수 관계 존재!
# 동전 간에 배수 관계가 존재하지 않는다면 탐욕법 성립하지 않음

import sys

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
A = [int(input_data()) for _ in range(N)]

cnt = 0
for i in range(N-1, -1, -1):
    if A[i] <= K:
        cnt += K//A[i]
        K %= A[i]
    elif K == 0:
        break
print(cnt)