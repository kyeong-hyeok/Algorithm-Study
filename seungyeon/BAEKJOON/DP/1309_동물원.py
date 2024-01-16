# dp[i][0] = i번째 줄에 아무 사자도 놓지 않는다.
# dp[i][1] = i번째 줄 1번째 칸에 사자를 놓는다.
# dp[i][2] = i번째 줄 2번째 칸에 사자를 놓는다.

n = int(input())

dp = [[0 for j in range(3)] for i in range(n+1)]

dp[1][0] = dp[1][1] = dp[1][2] = 1

for i in range(2,n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][2] = dp[i-1][0] + dp[i-1][1]

print(dp[n][0]+ dp[n][1]+dp[n][2]%9901)