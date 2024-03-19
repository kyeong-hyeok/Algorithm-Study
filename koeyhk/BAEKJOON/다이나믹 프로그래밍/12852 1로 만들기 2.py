# 1. 3으로 나누어 떨어질 때 나눔
# 2. 2로 나누어 떨어질 때 나눔
# 3. 1을 뺌
# N = 1,000,000 -> O(N) DP

from collections import deque

N = int(input())
dp = [1e9] * (N+1)
arr = [deque() for _ in range(N+1)]
dp[1] = 0
arr[1] = [1]

for i in range(2, N+1):
    if i % 3 == 0:
        dp[i] = dp[i//3] + 1
        arr[i] = [i] + arr[i//3]
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        arr[i] = [i] + arr[i//2]
    if dp[i-1] + 1 < dp[i]:
        dp[i] = dp[i-1] + 1
        arr[i] = [i] + arr[i-1]

print(dp[N])
print(' '.join(map(str, arr[N])), end='')
