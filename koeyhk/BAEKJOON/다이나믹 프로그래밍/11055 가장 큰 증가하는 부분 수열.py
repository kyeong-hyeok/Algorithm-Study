# 부분 수열 중 합이 가장 큰 것 구하기
# dp[i] = 0 ~ i까지의 수 중 증가하는 부분 수열의 최대 합

# 빠르게 생각하지 못했던 부분
# dp를 구하는 과정 -> for문으로 현재 인덱스 이전의 값들 조사 + 비교

import sys

input_data = sys.stdin.readline

N = int(input_data())
A = list(map(int, input_data().split()))
dp = A[:]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))