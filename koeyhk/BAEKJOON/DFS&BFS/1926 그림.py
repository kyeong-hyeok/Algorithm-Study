# 그림 개수, 가장 넓은 것의 넓이 출력
# 가로 or 세로로 연결 -> 연결이 된 그림
# 그림의 넓이 = 그림에 포함된 1의 개수

# 잘못 생각한 부분
# DFS로 그림의 모든 영역을 탐색하면 되겠다! -> 다른 방향으로 탐색 시 visited로 넓이 파악 불가능함
# 변수 w를 설정해 다른 방향으로 탐색한 부분도 넓이에 더해줘야 함

# BFS
# 변수 w를 설정해 탐색 시마다 w 증가

import sys
from collections import deque

input_data = sys.stdin.readline

n, m = map(int, input_data().split())
picture = [list(map(int, input_data().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    w = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and picture[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                w += 1
                q.append((nx, ny))
    return w


result = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and visited[i][j] == 0:
            result = max(result, bfs(i, j))
            cnt += 1
print(cnt)
print(result)


# DFS
# DFS 수행 시 인자로 w를 받고, w를 반환하여 그림의 넓이 구함

import sys
sys.setrecursionlimit(3000000)

input_data = sys.stdin.readline

n, m = map(int, input_data().split())
picture = [list(map(int, input_data().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, w):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and picture[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            w = dfs(nx, ny, w+1)
    return w


cnt = 0
result = 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            result = max(result, dfs(i, j, 1))
            cnt += 1

print(cnt)
print(result)