# 11 56
# 동기 n 명 = 500

# 잘못 생각한 부분
# 1. 친구의 친구 부르면 된까 dfs로 해도 되겠다! -> 친구의 친구까지만 부르는 것 제한해야함
# 2. dfs로 탐색하면서 제한하면 되겠다! -> dfs는 친구 한 명씩 깊이 탐색하기 때문에 문제가 됨
# ex) 1 2, 1 3, 2 3, 3 4일 때 친구 2, 친구 2의 친구 3 탐색 후에 친구 3 탐색하려고 하면 불가능!

# 다시 생각한 풀이
# BFS로 큐에 순서대로 탐색할 친구를 단계별로 넣으면 됨!

import sys
from collections import deque

input_data = sys.stdin.readline

n = int(input_data())
m = int(input_data())
friend = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input_data().split())
    friend[a].append(b)
    friend[b].append(a)


def bfs(x, r):
    q = deque()
    q.append((x, r))
    visited = [0] * (n + 1)
    visited[x] = 1
    while q:
        x, r = q.popleft()
        for f in friend[x]:
            if visited[f] == 0 and r < 2:
                visited[f] = 1
                q.append((f, r + 1))
    return visited


print(sum(bfs(1, 0)) - 1)
