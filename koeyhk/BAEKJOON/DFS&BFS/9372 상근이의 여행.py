# T = 100, N = 1000, M = 10000

import sys

input_data = sys.stdin.readline
T = int(input_data())


def dfs(x, r):
    for i in airplane[x]:
        if visited[i] == 0:
            visited[i] = 1
            r = dfs(i, r+1)
    return r


for _ in range(T):
    N, M = map(int, input_data().split())
    airplane = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input_data().split())
        airplane[a].append(b)
        airplane[b].append(a)
    visited = [0] * (N+1)
    visited[1] = 1
    print(dfs(1, 0))
