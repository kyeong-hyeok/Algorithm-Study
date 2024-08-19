# n = 500
# DP 풀이

import sys

input_data = sys.stdin.readline

n = int(input_data())
triangle = [list(map(int, input_data().split())) for _ in range(n)]
dp = [[0]*i for i in range(1, n+1)]
dp[0] = triangle[0]
for i in range(1, n):
    dp[i][0] += dp[i-1][0] + triangle[i][0]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    dp[i][i] += dp[i-1][i-1] + triangle[i][i]

print(max(dp[n-1]))