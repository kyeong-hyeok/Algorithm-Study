# 4 45
# i에서 j로 가는 길이가 양수인 경로 있는지
# N = 100

# BFS
# 76ms

import sys
from collections import deque
input_data = sys.stdin.readline

N = int(input_data())
edge = [[] for _ in range(N)]
for i in range(N):      # O(N^2)
    check = list(map(int, input_data().split()))
    for j in range(N):
        if check[j]:
            edge[i].append(j)


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in edge[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


for i in range(N):      # O(N^2)
    visited = [0] * N
    bfs(i)
    print(*visited)


# 플로이드 워셜 알고리즘
# 232ms

import sys

input_data = sys.stdin.readline

N = int(input_data())
edge = [list(map(int, input_data().split())) for _ in range(N)]


for k in range(N):      # O(N^3)
    for i in range(N):
        for j in range(N):
            if edge[i][k] and edge[k][j]:
                edge[i][j] = 1

for i in range(N):
    print(*edge[i])