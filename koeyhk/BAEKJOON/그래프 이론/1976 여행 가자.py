# N = 200, M = 1000
# 다음 도시로 이동 가능한지 여부를 각각 판단하면 됨 O(MN)
# 216ms

import sys

input_data = sys.stdin.readline

N = int(input_data())
M = int(input_data())
edge = [[] for _ in range(N+1)]
for i in range(1, N+1):
    e = list(map(int, input_data().split()))
    for j in range(N):
        if e[j]:
            edge[i].append(j+1)
plan = list(map(int, input_data().split()))


def dfs(x):
    for i in edge[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


p = 1
for i in range(M-1):
    visited = [0] * (N+1)
    visited[plan[i]] = 1
    dfs(plan[i])
    if visited[plan[i+1]] == 0:
        p = 0
        break

if p:
    print("YES")
else:
    print("NO")


# find_parent와 union을 이용한 이어진 정점 여부 확인
# 52ms

import sys

input_data = sys.stdin.readline

N = int(input_data())
M = int(input_data())
parent = [i for i in range(N+1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


for i in range(1, N+1):
    e = list(map(int, input_data().split()))
    for j in range(N):
        if e[j]:
            union(i, j+1)


plan = list(map(int, input_data().split()))
p = 1
for i in range(1, M):
    if parent[plan[0]] != parent[plan[i]]:
        p = 0
        break
if p:
    print("YES")
else:
    print("NO")