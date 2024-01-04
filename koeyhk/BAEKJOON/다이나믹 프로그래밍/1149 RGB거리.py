# N번째 집은 N-1, N+1번째 집과 색이 달라야 함
# 전에 선택한 색과 다르게만 하면 됨 -> dp[i] = [색1, 색2, 색3]

import sys

input_data = sys.stdin.readline

N = int(input_data())
dp = [list(map(int, input_data().split())) for _ in range(N)]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

print(min(dp[N - 1]))