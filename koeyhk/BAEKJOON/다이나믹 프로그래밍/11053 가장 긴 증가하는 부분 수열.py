# N = 1,000 -> O(N^2) 최대
# dp -> dp[i] = i번째 수를 포함하는 가장 긴 증가하는 부분 수열

import sys

input_data = sys.stdin.readline

N = int(input_data())
A = list(map(int, input_data().split()))
dp = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))