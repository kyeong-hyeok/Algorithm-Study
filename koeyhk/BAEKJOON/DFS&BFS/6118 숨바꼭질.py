# N = 20,000, M = 50,000
# O(N) -> BFS

import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input_data().split())
    num[A].append(B)
    num[B].append(A)


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        for i in num[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)


visited = [0] * (N+1)
bfs(1)
max_dis = max(visited)
print(visited.index(max_dis), max_dis-1, visited.count(max_dis))



