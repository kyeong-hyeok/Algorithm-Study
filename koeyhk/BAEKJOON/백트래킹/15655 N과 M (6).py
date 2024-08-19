# M, N = 8
# N개의 자연수 중 M개를 고른 수열 -> 오름차순
# 백트래킹 or 조합 -> 조합의 코드가 간단하긴 하다!


# 1. 백트래킹 문제 풀이

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
num.sort()
arr = []
visited = [0] * N


def bt(x):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(x, N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(num[i])
            bt(i+1)
            arr.pop()
            visited[i] = 0


bt(0)


# 조합 문제 풀이

import sys
from itertools import combinations
input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
num.sort()

for c in combinations(num, M):
    for i in c:
        print(i, end=' ')
    print()