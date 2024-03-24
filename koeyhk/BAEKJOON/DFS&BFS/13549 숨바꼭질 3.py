# 경우의 수 3가지 -> X-1, X+1, 2*X
# 백트래킹 -> 3^n
# DP -> 구현 방법이 떠오르지 않음
# BFS -> 3가지 경우로 큐에 저장

from collections import deque

N, K = map(int, input().split())
visited = [100000] * 200001


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        x = q.popleft()
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and visited[nx] > visited[x]:
                if nx == x*2:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
    return visited[K]


print(bfs(N))