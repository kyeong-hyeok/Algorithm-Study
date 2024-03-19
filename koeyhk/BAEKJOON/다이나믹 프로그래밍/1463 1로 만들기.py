# 1. DP -> Bottom Up 방식으로 N까지 수행

N = int(input())
dp = [i for i in range(N+1)]
if N >= 1:
    dp[1] = 0
for i in range(2, N+1):
    if i % 3 == 0:
        dp[i] = dp[i//3] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[N])


# 2. BFS + DP로 해결 가능
# N부터 3가지 경우의 수로 BFS 수행, 이미 계산한 값은 DP
# 아래 코드는 시간 초과 . . 이유는?

import sys
sys.setrecursionlimit(3000000)

N = int(input())
dp = [i for i in range(N+1)]
if N >= 1:
    dp[1] = 0


def bfs(x):
    if dp[x] != x:
        return dp[x]
    dp[x] = x
    if x % 3 == 0:
        dp[x] = min(dp[x], bfs(x//3)+1)
    if x % 2 == 0:
        dp[x] = min(dp[x], bfs(x//2)+1)
    dp[x] = min(dp[x], bfs(x-1)+1)
    return dp[x]


print(bfs(N))