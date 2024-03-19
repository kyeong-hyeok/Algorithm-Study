# 백트래킹
# -> 현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘
# 해를 구하는 도중 해가 아닐 때, 이전으로 돌아가 해를 찾는 기법
# DFS와의 차이점 -> 백트래킹은 아닐 때 더이상 진행하지 않음 (모든 경우 검색하지 않음)


# 1. 백트래킹

N, M = map(int, input().split())
arr = []
visited = [0] * (N+1)


def bt():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            bt()
            arr.pop()
            visited[i] = 0


bt()

# 2. 순열

from itertools import permutations

N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)

a = list(permutations(arr, M))

for i in a:
    for j in i:
        print(j, end=' ')
    print()

