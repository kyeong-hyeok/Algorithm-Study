# 4 46 5 26
# T = 1,000 W = 30
# DFS&BFS -> 2^30 시간 초과
# 움직이거나 움직이지 않거나 -> DP
# DP로 dp[i][j] = i초일 때 j번 움직였을 경우 [최댓값, 위치]
# i초일 때 for 문으로 횟수 그대로 or 늘려가면서 자두 개수 구하기

# 개선한 부분
# 움직인 횟수가 홀수이면 2번을 선택한 것, 움직인 횟수가 짝수이면 1번을 선택한 것
# dp[i][j] = i초일 때 j번 움직였을 경우의 최댓값

import sys

input_data = sys.stdin.readline

T, W = map(int, input_data().split())
drop = [int(input_data()) for _ in range(T)]
dp = [[0] * (W+2) for _ in range(T)]
if drop[0] == 1:
    dp[0][0] = 1
else:
    dp[0][1] = 1

for i in range(1, T):
    for j in range(W+1):
        if drop[i] == 1:        # 자두가 1번 나무에서 떨어질 때
            if j % 2 == 0:              # 전에 1번 나무에 있었다면
                dp[i][j] = max(dp[i-1][j]+1, dp[i][j])
            else:                       # 전에 2번 나무에 있었다면
                dp[i][j] = max(dp[i-1][j], dp[i][j])
                dp[i][j+1] = max(dp[i-1][j]+1, dp[i][j+1])
        else:                   # 자두가 2번 나무에서 떨어질 때
            if j % 2 == 1:              # 전에 2번 나무에 있었다면
                dp[i][j] = max(dp[i-1][j]+1, dp[i][j])
            else:                       # 전에 1번 나무에 있었다면
                dp[i][j] = max(dp[i-1][j], dp[i][j])
                dp[i][j+1] = max(dp[i-1][j]+1, dp[i][j+1])

print(max(dp[T-1][:W+1]))


# 처음 풀이

import sys

input_data = sys.stdin.readline

T, W = map(int, input_data().split())
drop = [int(input_data()) for _ in range(T)]
dp = [[[0, 0] for _ in range(W+2)] for _ in range(T)]
if drop[0] == 1:
    dp[0][0] = [1, 1]
else:
    dp[0][0] = [0, 1]
    dp[0][1] = [1, 2]
result = 0
for i in range(1, T):
    for j in range(W+1):
        if drop[i] == 1:        # 자두가 1번 나무에서 떨어질 때
            if dp[i-1][j][1] == 1:      # 전에 1번 나무에 있었다면
                if dp[i][j][0] < dp[i-1][j][0] + 1:     # 그대로 있기
                    dp[i][j] = [dp[i-1][j][0]+1, 1]
            else:                       # 전에 2번 나무에 있었다면
                if dp[i][j][0] < dp[i-1][j][0]:          # 그대로 있기
                    dp[i][j] = [dp[i-1][j][0], 2]
                if dp[i][j+1][0] < dp[i-1][j][0] + 1:    # 2번 나무로 이동하기
                    dp[i][j+1] = [dp[i-1][j][0]+1, 1]

        else:                   # 자두가 2번 나무에서 떨어질 때
            if dp[i-1][j][1] == 2:      # 전에 2번 나무에 있었다면
                if dp[i][j][0] < dp[i-1][j][0] + 1:     # 그대로 있기
                    dp[i][j] = [dp[i-1][j][0]+1, 2]
            else:                       # 전에 1번 나무에 있었다면
                if dp[i][j][0] < dp[i-1][j][0]:         # 그대로 있기
                    dp[i][j] = [dp[i-1][j][0], 1]
                if dp[i][j+1][0] < dp[i-1][j][0] + 1:   # 1번 나무로 이동하기
                    dp[i][j+1] = [dp[i-1][j][0]+1, 2]

result = 0
for i in range(W+1):
    result = max(result, dp[T-1][i][0])

print(result)