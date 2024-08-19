# 크루스칼 알고리즘
# 비용이 작은 길부터 싸이클이 형성되지 않을 경우 추가
# 마지막에 제일 큰 비용을 가진 경로를 빼면 두 부분으로 나누어짐

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
load = [list(map(int, input_data().split())) for _ in range(M)]
load.sort(key=lambda x : x[2])
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result, last = 0, 0
for a, b, c in load:    # O(M)
    if find_parent(a) != find_parent(b):
        union(a, b)
        result += c
        last = c
print(result - last)


# 시간 초과 풀이
# BFS + 탐욕법
# N(100,000)개 집, M(1,000,000)개 길
# 마을에 집 하나 이상, 마을 안에 집 모두 연결
# 길 지워보고 전체 경로가 두 개이면?

import sys
from collections import deque
input_data = sys.stdin.readline

N, M = map(int, input_data().split())
load = [list(map(int, input_data().split())) for _ in range(M)]
load.sort(key=lambda x : x[2])
edge = [[] for _ in range(N+1)]


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        for i in edge[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


result = 0
j = 0
for l in load:
    a, b, c = l[0], l[1], l[2]
    edge[a].append(b)
    edge[b].append(a)
    j += 1
    result += c
    if j < (N//2-1)*2:  # 최소 있어야 하는 길의 수
        continue
    visited = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i)
            cnt += 1
        if cnt > 2:
            break
    if cnt == 2:
        print(result)
        break