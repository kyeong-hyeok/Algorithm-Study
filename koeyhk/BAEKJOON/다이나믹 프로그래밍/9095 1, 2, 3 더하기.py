# DP로 X-3, X-2, X-1에서 더하기
# D[4]
# 1+1+1+(1), 3+(1), 2+1+(1), 1+2+(1) -> D[3]
# 1+1+(2), 2+(2) -> D[2]
# 1+(3) -> D[1]

# 놓친 부분
# 문제에서 1+2, 2+1을 다른 경우의 수로 취급함!

T = int(input())
dp = [i for i in range(12)]
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
for i in range(T):
    n = int(input())
    print(dp[n])