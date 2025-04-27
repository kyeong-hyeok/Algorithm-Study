import sys
input=sys.stdin.readline


n=int(input())
arr=list(map(int,input().split()))
dp=[1]*n
for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]: # 해당 값이 이전 값보다 크다면
            dp[i] = max(dp[i],dp[j] + 1)

print(max(dp))

answer=[]
order=max(dp)

for i in range(n-1,-1,-1): # 뒤에서부터 순서대로 
    if dp[i] == order:
        answer.append(arr[i])
        order -= 1

answer.reverse()
print(*answer)