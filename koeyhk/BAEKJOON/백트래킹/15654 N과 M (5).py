# N개의 자연수 중 M개를 고른 수열
# N, M = 8 -> 시간 복잡도 낮음

# 1. 백트래킹

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
arr = []
visited = [0] * N
num.sort()


def bt(x):
    if len(arr) == M:
        for a in arr:
            print(a, end=' ')
        print()
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(num[i])
            bt(i+1)
            arr.pop()
            visited[i] = 0


bt(0)

# 2. 순열

import sys
from itertools import permutations

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
num.sort()
per = list(permutations(num, M))
for pe in per:
    for p in pe:
        print(p, end=' ')
    print()