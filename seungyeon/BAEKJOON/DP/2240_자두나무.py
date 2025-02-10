import sys

input = sys.stdin.readline

t,w=map(int,input().split())
arr = [0] + [int(input()) for _ in range(t)]


dp=[[0] * (w+1) for _ in range(t+1)]
dp[1][0],dp[1][1] = arr[1]%2, arr[1]//2

for t in range(2,t+1):
    for w in range(w+1):

        if w % 2 == 0:
            j = arr[t] % 2 
        else:
            j = arr[t] // 2

        dp[t][w] = max(dp[t-1][0:w+1]) + j

print(max(dp[-1]))