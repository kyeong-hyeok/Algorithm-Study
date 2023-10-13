# N <= 1000 -> 길이가 1000인 수는 완전 탐색 불가능
# DP를 이용해서 중복되는 경우의 수 줄이기?
# dp[1] = 1 + 1 + 1 + ... + 1
# dp[2] = 1 + 2 + 3 + ... + 10
# dp[3] = 1 + 3 + 6 + ... +

N = int(input())
dp = [[1] * 10 for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(1, 10):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007

print(sum(dp[N])%10007)