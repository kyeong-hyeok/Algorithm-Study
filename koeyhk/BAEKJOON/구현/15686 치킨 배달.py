# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리, 0 빈칸, 1 집, 2 치킨집

# 첫 번째 풀이
# 치킨집 중에 M개 선택한 조합 만들어서 치킨집마다 bfs 수행 -> 집까지의 거리 갱신
# N 50, M 13 -> 13C6*13*50log50 시간 초과날 수도 있음

import sys
from itertools import combinations
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
city = [list(map(int, input_data().split())) for _ in range(N)]
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
comb = list(combinations(chicken, M))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동할 곳이 이전에 방문했던 때보다 더 빨리 방문 가능하다면 방문
            if 0 <= nx < N and 0 <= ny < N and (visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


min_d = 10e9
for c in comb:
    result = 0
    visited = [[0] * N for _ in range(N)]
    # 치킨집마다 BFS (치킨집 최대 개수 13개)
    for i in c:
        bfs(i[0], i[1], visited)
    for h in home:
        result += visited[h[0]][h[1]] - 1
    min_d = min(min_d, result)

print(min_d)

# 두 번째 풀이
# ** 문제에서 집과 치킨집과의 거리 구하는 것이 힌트 - 좌표 뺄셈 절댓값 **
# 집에서 가장 가까운 치킨집까지의 거리를 반환하는 함수 만들기
# 100*13*13C6 시간 복잡도 낮음

import sys
from itertools import combinations

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
city = [list(map(int, input_data().split())) for _ in range(N)]
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
comb = list(combinations(chicken, M))


def chicken_dis(h, chicken):
    min_dis = 10e9
    for c in chicken:
        dis = abs(h[0]-c[0]) + abs(h[1]-c[1])
        min_dis = min(min_dis, dis)
    return min_dis


result = 10e9
for c in comb:
    city_dis = 0
    for h in home:
        city_dis += chicken_dis(h, c)
    result = min(result, city_dis)
print(result)