# 2행 n열
# n = 100,000

# 백트래킹 -> 시간 초과, DP -> O(n)
# 각각의 행마다 따로 DP? -> 정확한 값을 만들기 어려움
# 처음 열부터 마지막 열부터 두 행 각각에 DP 적용
# DP[i][n] = i행에서 n열 스티커를 포함시켜 골랐을 경우 최대 가치

import sys

input_data = sys.stdin.readline

T = int(input_data())
for _ in range(T):
    n = int(input_data())
    dp = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    for i in range(2, n):
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][n - 1], dp[1][n - 1]))