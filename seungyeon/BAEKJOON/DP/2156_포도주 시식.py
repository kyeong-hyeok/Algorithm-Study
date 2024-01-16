# 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록

n = int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

# 3잔 연속해서 마실 수 없음
# i-2 /  i -1 / i
# 1 0 0
# 1 1 0
# 1 0 1
# 0 1 1
# 0 0 1
# 0 1 0

dp=[0]*10000

dp[0]=arr[0]
dp[1]=arr[0] + arr[1]
dp[2] = max(arr[2]+arr[0],arr[2]+arr[1],dp[1])

for i in range(3,n):
  dp[i] = max (dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i],dp[i-1])

print(max(dp))
