# 1. 테이블 정의하기
# -> i번째 계단을 밟았을 때 점수 합의 최댓값
# 2. 점화식 찾기
# 3. 초기값 정하기

# 한 계단 or 두 계단씩 오를 수 있음, 연속된 세 계단 x, 마지막 계단은 밟기

# 1 -> 1
# 2 -> 1, 2
# 3 -> 1, 3 or 2, 3
# 4 -> 1, 2, 4 or 1, 3, 4
# 5 -> 1, 2, 4, 5 or 1, 3, 5 or 2, 3, 5 -> dp[n-2] + n, dp[n-3] + (n-1) + (n)
# 6 -> 1, 2, 4, 6 or 1, 3, 4, 6 or 1, 3, 5, 6 or 2, 3, 5, 6

import sys

input_data = sys.stdin.readline

N = int(input_data())
stair = [int(input_data()) for _ in range(N)]
dp = [0] * (N+1)
if N > 0:
    dp[0] = stair[0]
if N > 1:
    dp[1] = stair[0] + stair[1]
if N > 2:
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3, N):
    dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]

print(dp[N-1])