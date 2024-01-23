# N = 100 -> O(10000) * O(100)

# 문제 풀이 아이디어
# 비의 양에 따른 DFS -> visited 리스트를 따로 설정하지 않아도 잠긴 지역을 0으로 만들어주면 DFS 가능!
# 지역의 높이가 비의 양보다 클 때만 DFS 수행, result += 1

import sys
sys.setrecursionlimit(10**9)
input_data = sys.stdin.readline

N = int(input_data())
height = [list(map(int, input_data().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def dfs(x, y, h, i):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and h[nx][ny] > i:
            h[nx][ny] = 0
            dfs(nx, ny, h, i)


answer = 0
for i in range(101):
    h = [he[:] for he in height]
    result = 0
    for x in range(N):      # O(N^2)
        for y in range(N):
            if h[x][y] > i:
                result += 1
                dfs(x, y, h, i)
    answer = max(answer, result)


print(answer)