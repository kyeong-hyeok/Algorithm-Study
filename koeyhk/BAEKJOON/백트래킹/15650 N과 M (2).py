# 1. 백트래킹

N, M = map(int, input().split())
visited = [0] * (N+1)
arr = []


def bt(x):
    if len(arr) == M:
        for a in arr:
            print(a, end=' ')
        print()
        return
    for i in range(x, N+1):
        if visited[i] == 0:
            arr.append(i)
            visited[i] = 1
            bt(i+1)
            visited[i] = 0
            arr.pop()


bt(1)


# 2. 조합

from itertools import combinations
N, M = map(int, input().split())
num = [i for i in range(1,N+1)]
comb = list(combinations(num, M))

for c in comb:
    for i in range(M):
        print(c[i], end=' ')
    print()

