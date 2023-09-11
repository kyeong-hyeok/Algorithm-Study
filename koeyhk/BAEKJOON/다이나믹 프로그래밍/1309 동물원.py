N = int(input())
dp = [0] * (N+1)
dp[0], dp[1] = 1, 3
for i in range(2, N+1):
    # 이전 우리에 사자가 없을 경우 + 사자가 있을 경우
    dp[i] = (dp[i-2] + dp[i-1] * 2) % 9901
print(dp[N])