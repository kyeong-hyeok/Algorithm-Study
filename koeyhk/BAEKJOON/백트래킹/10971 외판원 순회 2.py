# N = 10

# 생각하지 못 했던 부분
# 마지막 도시에서 돌아갈 때 첫 도시로 가지 못 할 수도 있음

import sys

input_data = sys.stdin.readline

N = int(input_data())
cost = [list(map(int, input_data().split())) for _ in range(N)]
result = 10**9
visited = [0] * N


def bt(x, r, k, cnt):
    global result
    if cnt == N-1:
        if cost[x][k]:
            result = min(result, r+cost[x][k])
        return
    if r > result:      # 시간 단축
        return
    for i in range(N):
        if k != i and visited[i] == 0 and cost[x][i] != 0:
            visited[i] = 1
            bt(i, r+cost[x][i], k, cnt+1)
            visited[i] = 0


for i in range(N):
    bt(i, 0, i, 0)
print(result)