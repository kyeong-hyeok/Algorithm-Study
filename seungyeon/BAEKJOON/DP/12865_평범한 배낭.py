import sys

input=sys.stdin.readline

n,k=map(int,input().split(" "))


dp=[[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w,v=map(int,input().split(" ")) # 무게,가치

    for j in range(1,k+1):

        if j < w: # 가방 크기가 내가 무게보다 작으니까 
            dp[i][j] = dp[i-1][j] 
        else:
            dp[i][j] = max(dp[i-1][j],v+dp[i-1][j-w])

print(dp[n][k])