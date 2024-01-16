import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, []] for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, n + 1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]

    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

print(dp[n][0])
print(*reversed(dp[n][1]))



# from collections import deque

# n = int(input())
# que = deque()
# que.append([n])
# answer = []

# while que:
#     a = que.popleft()
#     x = a[0]
#     if x == 1:
#         answer = a
#         break

#     if x % 3 == 0:
#         que.append([x // 3] + a)

#     if x % 2 == 0:
#         que.append([x // 2] + a)
    
#     que.append([x - 1] + a)

# print(len(answer) - 1)
# print(*answer[::-1])