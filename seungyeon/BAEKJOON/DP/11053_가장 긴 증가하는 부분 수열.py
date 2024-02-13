import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

dp=[0] * n
dp[0] = 1
dp[1] = 2 if arr[0] < arr[1] else 1

for i in range(1,len(arr)):
    dp[i] = dp[i-1] + 1 if arr[i-1] < arr[i] else dp[i-1]
print(dp[n-1])