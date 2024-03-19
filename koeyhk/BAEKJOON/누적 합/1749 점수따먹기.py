# N, M = 200
# 누적합 -> 부분행렬 마다 확인하기

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
matrix = [list(map(int, input_data().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]
result = -10e9
for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(i, N+1):
            for h in range(j, M+1):
                result = max(result, dp[k][h] - dp[i-1][h] - dp[k][j-1] + dp[i-1][j-1])
print(result)