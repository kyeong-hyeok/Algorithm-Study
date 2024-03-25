# 하루가 지날 때마다 중량 K만큼 감소
# 운동 키트 N일 동안 한 번씩 사용 가능 -> 항상 중량 500 이상 유지
# N = 8, K = 50
# 백트래킹 or 순열

import sys

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
A = list(map(int, input_data().split()))
result = 0
visited = [0] * N


def bt(o, cnt):
    global result
    if cnt == N:
        result += 1
        return
    for i in range(N):
        if visited[i] == 0 and o-K+A[i] >= 500:
            visited[i] = 1
            bt(o-K+A[i], cnt+1)
            visited[i] = 0


bt(500, 0)
print(result)