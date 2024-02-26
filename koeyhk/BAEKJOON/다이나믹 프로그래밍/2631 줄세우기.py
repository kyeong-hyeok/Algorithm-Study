# N = 200

# 생각하지 못 한 부분
# 안 바꿔도 되는 번호의 개수를 파악해야 함
# dp -> dp[i] = i번째 수를 포함하는 가장 긴 증가하는 부분 수열
# N - (dp의 최댓값)

import sys

input_data = sys.stdin.readline

N = int(input_data())
line = [int(input_data()) for _ in range(N)]
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))