# N = 125
# 가중치(각 장소에서 잃는 루피)가 다름
# -> 잃는 최소 루피를 구하기 위해 다익스트라 알고리즘 사용
# 시간 복잡도 O(NlogN)

import heapq
import sys
sys.setrecursionlimit(10**9)
input_data = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dijkstra(x, y):
    q = []
    heapq.heappush(q, (visited[x][y], (x, y)))
    while q:
        a, xy = heapq.heappop(q)
        for i in range(4):
            nx = xy[0] + dx[i]
            ny = xy[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] > a + rupy[nx][ny]:
                visited[nx][ny] = a + rupy[nx][ny]
                heapq.heappush(q, (visited[nx][ny], (nx, ny)))


i = 1
while 1:
    N = int(input_data())
    if N == 0:
        break
    rupy = [list(map(int, input_data().split())) for _ in range(N)]
    visited = [[10 ** 9] * N for _ in range(N)]
    visited[0][0] = rupy[0][0]
    dijkstra(0, 0)
    print(f'Problem {i}: {visited[N-1][N-1]}')
    i += 1

    

# 이전 풀이 -> DFS 시간 초과

import sys
sys.setrecursionlimit(10**9)
input_data = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] > visited[x][y] + rupy[nx][ny]:
            visited[nx][ny] = visited[x][y] + rupy[nx][ny]
            dfs(nx, ny)


i = 1
while 1:
    N = int(input_data())
    if N == 0:
        break
    rupy = [list(map(int, input_data().split())) for _ in range(N)]
    visited = [[10**9]*N for _ in range(N)]
    visited[0][0] = rupy[0][0]
    dfs(0, 0)
    print(f'Problem {i}: {visited[N-1][N-1]}')
    i += 1