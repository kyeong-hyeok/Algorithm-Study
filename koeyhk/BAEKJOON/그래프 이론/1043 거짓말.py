# 집합 연산을 이용한 풀이
# 교집합이 존재한다면 -> union

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
t = set(input_data().split()[1:])
party = [set(input_data().split()[1:]) for _ in range(M)]

for _ in range(M):
    for p in party:
        if p & t:
            t = t.union(p)

result = 0
for p in party:
    if p & t:
        continue
    result += 1
print(result)


# 이전 풀이
# N, M = 50
# M번 전체 파티를 돌면서 진실 아는 사람이 있는 파티 union

# 처음에 생각하지 못한 부분
# 진실 얘기한 사람이 있는 파티 사람들을 진실 아는 사람에 추가해둔 다음에 다른 파티 탐색


import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
t = list(map(int, input_data().split()))
party = [list(map(int, input_data().split())) for _ in range(M)]
parent = [i for i in range(N+1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(1, len(t)):
    union(0, t[i])


for _ in range(M):
    i = 0
    while i < M:
        j = 1
        p = 0
        while j < len(t):
            if t[j] in party[i][1:]:
                p = 1
                break
            j += 1
        if p:
            for j in range(1, len(party[i])):
                if find_parent(0) != find_parent(party[i][j]):
                    union(0, party[i][j])
                    t.append(party[i][j])
        i += 1

result = 0
for i in party:
    p = 0
    for j in range(1, len(i)):
        if find_parent(0) != find_parent(i[j]):
            p = 1
            break
    if p:
        result += 1

print(result)