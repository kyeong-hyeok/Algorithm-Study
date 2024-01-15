# n = 100

import sys

input_data = sys.stdin.readline

n = int(input_data())
m = int(input_data())
edge = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input_data().split())
    edge[a].append(b)
    edge[b].append(a)


def dfs(x):
    global result
    for i in edge[x]:
        if visited[i] == 0:
            result += 1
            visited[i] = 1
            dfs(i)


result = 0
visited = [0] * (n+1)
visited[1] = 1
dfs(1)
print(result)