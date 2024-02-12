import sys
input=sys.stdin.readline

n = int(input())


#중복되지 않으려면
# 마지막 자리가 0일 때 , 마지막 자리가 1일 때 
# 마지막 자리가 1이라면 이전에 1이 오면 안됨


dp=[[0]*2  for _ in range ( n+1)]
dp[0][0] = 0
dp[0][1] =  0

if n > 0:
    dp[1][0] = 0
    dp[1][1] =  1

if n > 1:
    dp[2][0] = 1
    dp[2][1] = 0

if n > 2:
    for i in range(3,n+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]

print(dp[n][0]+dp[n][1])
