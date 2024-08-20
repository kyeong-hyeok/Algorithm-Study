# NxN(20x20), 물고기 M마리, 아기 상어 1마리
# 크기 작은거 먹을 수 있음, 같은 거 지나갈 수 있음
# 먹을 수 있는 거 없다면 엄마한테 도움 요청
# 먹을 수 있는 거 한마리면 먹기
# 먹을 수 있는 거 두마리 이상이면 거리 가장 가까운 거 (가장 위 -> 가장 왼쪽)
# 크기와 같은 수의 물고기 먹어야 1 증가

# 놓친 부분
# 먹을 물고기가 있더라도 못 가는 경우가 있음 . . !

import sys
from collections import deque
input_data = sys.stdin.readline

N = int(input_data())
space = [list(map(int, input_data().split())) for _ in range(N)]
fish = []
for i in range(N):
    for j in range(N):
        if 1 <= space[i][j] <= 7:
            fish.append((i, j, space[i][j]))
        elif space[i][j] == 9:
            x, y = i, j
            space[i][j] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# BFS 최단 거리
def bfs(ax, ay, aa, ab, size):
    q = deque()
    q.append((ax, ay))
    visited = [[0]*N for _ in range(N)]
    visited[ax][ay] = 1
    while q:
        ax, ay = q.popleft()
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and space[nx][ny] <= size:
                visited[nx][ny] = visited[ax][ay] + 1
                q.append((nx, ny))
                if nx == aa and ny == ab:
                    return visited[nx][ny] - 1
    return -1


# 물고기 먹으러 다니기
t, cnt, p, a, b = 0, 0, 0, 0, 0
size = 2
while 1:
    if len(fish) == 0 or p:
        break
    else:
        dis = 500
        for i in range(len(fish)):
            if fish[i][2] < size:
                d = bfs(x, y, fish[i][0], fish[i][1], size)
                if d == -1:
                    continue
                if d < dis or ((d == dis) and (fish[i][0] < a or (fish[i][0] == a and fish[i][1] < b))):
                    a, b = fish[i][0], fish[i][1]
                    dis = d
        if dis != 500:
            t += dis
            x, y = a, b
            z = 0
            while z < len(fish):
                if fish[z][0] == a and fish[z][1] == b:
                    del fish[z]
                    break
                z += 1
            space[a][b] = 0
            cnt += 1
            if cnt == size:
                size += 1
                cnt = 0
        else:
            p = 1

print(t)


