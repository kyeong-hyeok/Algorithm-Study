# 마지막 계단을 밟아야한다 
# 2칸 전 + 1칸전 
# 총 점수의 최댓값

import sys
input=sys.stdin.readline

n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

dp=[0 for _ in range(n)]


if n < 2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]

    for j in range(2,n):
        dp[j] = max(dp[j-2]+arr[j], dp[j-3]+arr[j-1]+ arr[j])

    print(dp[-1])
