import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(" "))))


dp=[0 for i in range(n+1)]

for i in range(n-1,-1,-1):
    if i + arr[i][0] > n:
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1],arr[i][1] + dp[i+arr[i][0]]) # arr[i][0] 이걸 선택했을 때의 값과 이전 뒤에서의 값을 비교

print(dp[0])