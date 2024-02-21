# N, M = 50,000 C = 1,000
# 다익스트라 알고리즘 - 시간 복잡도 O(MlogN)

# 가중치가 다른 상황에서 최단 경로를 찾을 때 -> 다익스트라 알고리즘

import heapq
import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input_data().split())
    edge[A].append((B, C))
    edge[B].append((A, C))
distance = [10 ** 9] * (N + 1)


def dijkstra(x):
    distance[x] = 0
    q = []
    heapq.heappush(q, (0, x))
    while q:
        cost, x = heapq.heappop(q)
        if distance[x] < cost:
            continue
        for a, c in edge[x]:
            if distance[a] > cost + c:
                distance[a] = cost + c
                heapq.heappush(q, (distance[a], a))


dijkstra(1)
print(distance[N])


# 가중치가 동일하지 않아 최단 경로를 보장할 수 없다고 생각하는데 BFS로 풀었을 때 통과되는 이유는?

import sys
from collections import deque
input_data = sys.stdin.readline

N, M = map(int, input_data().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input_data().split())
    edge[A].append((B, C))
    edge[B].append((A, C))


def bfs(x):
    q = deque()
    visited = [10**9] * (N+1)
    visited[x] = 0
    q.append((x, 0))
    while q:
        x, c = q.popleft()
        for i in edge[x]:
            a, cost = i[0], i[1]
            if visited[a] > visited[x] + cost:
                visited[a] = visited[x] + cost
                q.append((a, visited[a]))
    return visited[N]


print(bfs(1))

