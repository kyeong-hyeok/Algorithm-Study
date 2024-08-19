import sys

input_data = sys.stdin.readline

n = int(input_data())
wine = []
for i in range(n):
    wine.append(int(input_data()))

dp = [0 for _ in range(n)]
if n >= 1:
    dp[0] = wine[0]
if n >= 2:
    dp[1] = dp[0] + wine[1]
if n >= 3:
    dp[2] = max(wine[0]+wine[1], wine[0]+wine[2], wine[1]+wine[2])
for i in range(3, n):
    # (i-3)까지 최대 양 + (i-1) + (i) | (i-2)까지 최대 양 + (i) | (i-1)까지 최대 양
    dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])

print(dp[n-1])