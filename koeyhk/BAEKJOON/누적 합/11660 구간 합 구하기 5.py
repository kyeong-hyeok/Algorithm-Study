# N = 1024, M = 100,000
# 성능 개선 풀이
# x, y까지 누적합을 구한 결과 저장 -> O(MN) -> O(N^2) 시간 단축

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
board = [list(map(int, input_data().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]
s = 0
for i in range(1, N+1):      # O(N^2)
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + board[i-1][j-1]
for _ in range(M):      # O(M)
    x1, y1, x2, y2 = map(int, input_data().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)


# 이전 풀이
# x, y까지 모든 요소합을 구한 결과 저장 -> O(MN)
# Python3으로 통과 x, pypy3로 통과

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
board = [list(map(int, input_data().split())) for _ in range(N)]
sum_b = [[0]*N for _ in range(N)]
s = 0
for i in range(N):      # O(N^2)
    for j in range(N):
        s += board[i][j]
        sum_b[i][j] = s
for _ in range(M):      # O(MN)
    x1, y1, x2, y2 = map(int, input_data().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    result = 0
    for i in range(x1, x2+1):
        result += sum_b[i][y2] - sum_b[i][y1] + board[i][y1]
    print(result)