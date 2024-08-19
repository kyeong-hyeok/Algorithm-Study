# N = 20(짝수)
# 조합 -> 20C10
# Python3 -> 3652 ms

import sys
from itertools import combinations

input_data = sys.stdin.readline

N = int(input_data())
S = [list(map(int, input_data().split())) for _ in range(N)]
num = [i for i in range(N)]
l = N//2
result = 10e9
comb = list(combinations(num, l))
for c in range(len(comb)//2):
    r1, r2 = 0, 0
    tmp = list(set(num) - set(comb[c]))
    for i in range(l):  # O(100)
        for j in range(l):
            if i != j:
                r1 += S[comb[c][i]][comb[c][j]]
                r2 += S[tmp[i]][tmp[j]]
    result = min(result, abs(r1-r2))

print(result)

# 백트래킹
# 생각하지 못 했던 풀이
# 백트래킹으로 N//2 개의 수를 방문하고 각 팀 능력치의 합 구하기
# 6152 ms

import sys

input_data = sys.stdin.readline

N = int(input_data())
S = [list(map(int, input_data().split())) for _ in range(N)]
visited = [0] * N
result = 10e9
l = N//2


def bt(x, L):
    global result
    if L == l:
        A, B = 0, 0
        for i in range(N):      # O(400)
            for j in range(N):
                if visited[i] and visited[j]:
                    A += S[i][j]
                elif not visited[i] and not visited[j]:
                    B += S[i][j]
        result = min(result, abs(A-B))
        return
    for i in range(x, N):
        visited[i] = 1
        bt(i+1, L+1)
        visited[i] = 0


bt(0, 0)
print(result)