# 행성의 개수 N = 10
# 이미 방문한 행성도 중복해서 갈 수 있음

# 처음 생각한 풀이
# K에서 BFS로 최단 시간 구하기
# 현재 시간보다 길면 return

# 문제 풀이
# 중복 방문 가능 -> 행성 i에서 j로 가는 최솟값 먼저 구하기 (플로이드 워셜)
# 백트래킹으로 방문한 행성 제외하고 방문

# 궁금한 점
# 플로이드 워셜을 사용하면 그 과정에서 방문하는 지점이 생기는데 결과에 영향을 가지 않을까?
# 이미 방문한 지점을 다시 방문하는 경우가 생길 수 있지 않나?

import sys
sys.setrecursionlimit(10**9)

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
T = [list(map(int, input_data().split())) for _ in range(N)]
result = 10e9
visited= [0] * N

for k in range(N):
    for i in range(N):
        for j in range(N):
            T[i][j] = min(T[i][j], T[i][k] + T[k][j])


def bt(x, cnt, time):
    global result
    if time > result:
        return
    if cnt == N:
        result = time
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            bt(i, cnt+1, time + T[x][i])
            visited[i] = 0


visited[K] = 1
bt(K, 1, 0)
print(result)