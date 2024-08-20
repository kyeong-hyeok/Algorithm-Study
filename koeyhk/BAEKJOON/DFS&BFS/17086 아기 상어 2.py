# N, M = 50
# BFS로 <최소> 거리 갱신 -> <최대> 안전 거리 구하기

# 문제 조건에서 놓친 부분
# 이동은 인접합 8방향(대각선 포함)

# 개선한 풀이
# safe 리스트 삭제, 상어가 있는 부분 미리 큐에 넣고 BFS
# 68ms

import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
space = [list(map(int, input_data().split())) for _ in range(N)]
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
q = deque()


def bfs():
    result = 0
    while q:
        x, y, k = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and space[nx][ny] == 0:
                space[nx][ny] = k + 1
                q.append((nx, ny, k+1))
                result = max(result, space[nx][ny])
    return result


for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            q.append((i, j, 0))
print(bfs())


# 이전 풀이
# 136ms

import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
space = [list(map(int, input_data().split())) for _ in range(N)]
safe = [[100000]*M for _ in range(N)]
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, k = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and space[nx][ny] == 0 and safe[nx][ny] > k + 1:
                safe[nx][ny] = k + 1
                q.append((nx, ny, k+1))


for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            bfs(i, j)

result = 0
for i in range(N):
    for j in range(M):
        if space[i][j] == 0:
            result = max(result, safe[i][j])

print(result)