# N = 1000, M = 10,000 -> BFS, DFS - O(N)
# 문제 잘 읽기 -> 정점 번호가 작은 것을 먼저 방문!

import sys
from collections import deque

input_data = sys.stdin.readline

N, M, V = map(int, input_data().split())
edge = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input_data().split())
    edge[a].append(b)
    edge[b].append(a)

for e in edge:
    e.sort()


def dfs(x):
    if x <= 0 or x > N:
        return
    visited[x] = 1
    print(x, end=' ')
    for e in edge[x]:
        if visited[e] == 0:
            dfs(e)
    return


def bfs(x):
    q = deque()
    q.append(x)
    visited = [0] * (N+1)
    visited[x] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for e in edge[x]:
            if visited[e] == 0:
                q.append(e)
                visited[e] = 1


visited = [0] * (N+1)
dfs(V)
print()
bfs(V)