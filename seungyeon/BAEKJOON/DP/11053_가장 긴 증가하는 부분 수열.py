import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

dp = [1] * n
for i in range(1,n):  # 현재 위치에 있는 값이 이전 원소보다 큰지 확인
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

# dp=[0] * n
# dp[0] = 1
# dp[1] = 2 if arr[0] < arr[1] else 1

# for i in range(1,len(arr)):
#     dp[i] = dp[i-1] + 1 if arr[i-1] < arr[i] else dp[i-1]
# print(max(dp))