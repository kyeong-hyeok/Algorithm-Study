import sys
input=sys.stdin.readline

n,s,m=map(int,input().split(" "))
arr=list(map(int,input().split(" ")))

dp=[0,0]*(n+1)

for i in range(n):

    if 0< max(dp[i-1])+arr[i] < m :
        dp[i][0] = max(dp[i-1])+arr[i]
    else:
        dp[i][0] = max(dp[i-1])

    if 0 < max(dp[i-1])-arr[i] < m:
        dp[i][1] = max(dp[i-1])-arr[i]
    else:
        dp[i][1] = max(dp[i-1])

print(max(dp[n]))


# dp[n] 이 max 이려면