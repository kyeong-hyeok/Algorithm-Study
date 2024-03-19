# 7 50
# N+1 일째 되는 날 퇴사 - N일 동안 많은 상담
# N = 1,500,000 T = 50 P = 1,000
# (과거의 P 최댓값(dp[i]) + 현재 상담 P), dp[i+T] 중 최댓값을 dp[i+T]에 저장

import sys

input_data = sys.stdin.readline

N = int(input_data())
tp = [list(map(int, input_data().split())) for _ in range(N)]
dp = [0] * (N+51)
for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    k = i + tp[i-1][0]
    dp[k] = max(dp[k], dp[i] + tp[i-1][1])
dp[N+1] = max(dp[N], dp[N+1])
print(dp[N+1])