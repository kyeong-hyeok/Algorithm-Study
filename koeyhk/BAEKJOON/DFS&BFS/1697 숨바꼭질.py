# 11 17
# N, K = 100,000
# 걷기: X-1, X+1  순간이동: 2*X
# K에서 2 나누거나 1 빼거나 1 더하기

# 잘못 생각한 부분
# 1차원 좌표에서 1을 더하거나 빼고 곱하는 형태이므로, DP로 접근하여 최솟값을 구하려고 했다.
# Bottom-Up 방식으로 할 경우 x+1과 같이 이후 값을 참조해야 하므로 DP를 적용하기에는 어려움이 있었다.

# BFS로 접근하면 문제를 간단히 풀 수 있었다!
# 문제 풀이 전 접근 방식에 대한 검증이 필요할 것 같다.

from collections import deque

N, K = map(int, input().split())
visited = [1e9] * (200001)


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and visited[nx] > visited[x] + 1:
                q.append(nx)
                visited[nx] = visited[x] + 1


bfs(N)
print(visited[K] - 1)