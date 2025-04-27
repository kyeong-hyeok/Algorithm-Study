# 9 55
# n, m = 1000 -> 1000 x 1000

# 생각하지 못한 부분
# 정사각형 -> 인접한 4개의 칸으로 확인

import sys

input_data = sys.stdin.readline

n, m = map(int, input_data().split())
board = [list(map(int, input_data().rstrip())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = board[i][j]
        elif board[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        result = max(result, dp[i][j])

print(result*result)


# 이전 풀이
# 현재 지점에서 오른쪽에 연속으로 존재하는 1의 수 구함
# -> 아래로 내려가면서 정사각형 크기 결정
# 실패

import sys

input_data = sys.stdin.readline

n, m = map(int, input_data().split())
board = [list(map(int, input_data().rstrip())) for _ in range(n)]
count = [[0]*m for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(m-1, -1, -1):
        if board[i][j] == 1:
            cnt += 1
        else:
            cnt = 0
        count[i][j] = cnt

result = 0
for i in range(n):
    for j in range(m):
        if count[i][j] > result:
            cnt = max(n-i, count[i][j])
            r = 1
            k = i + 1
            while k < i + cnt and k < n:
                if count[k][j] < cnt:
                    if count[k][j] <= k-i+1:
                        r = max(k-i, count[k][j])
                        k += cnt
                    else:
                        cnt = count[k][j]
                        if k == n-1:
                            r = count[k][j]
                elif k == n-1:
                    r = k-i+1
                k += 1
            result = max(result, r)


print(result*result)