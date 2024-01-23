# N, M = 50  K = 2500 -> DFS O(N*M)

# 문제에서 시간을 오래 쓴 부분
# 디버깅 ny = y + dy[i]에서  ny = y = dy[i] 라고 함 . .

# 개선할 수 있는 부분
# visited를 만들지 않고, 이미 지나간 지역은 0으로 바꾸면 됨!

import sys
sys.setrecursionlimit(10**9)
input_data = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and ground[nx][ny] == 1:
            ground[nx][ny] = 0
            dfs(nx, ny)


T = int(input_data())
for i in range(T):
    M, N, K = map(int, input_data().split())
    ground = [[0]*M for _ in range(N)]
    bae = []
    for _ in range(K):
        x, y = map(int, input_data().split())
        ground[y][x] = 1
        bae.append((y, x))
    result = 0
    for b in bae:
        if ground[b[0]][b[1]] == 1:
            ground[b[0]][b[1]] = 0
            dfs(b[0], b[1])
            result += 1
    print(result)