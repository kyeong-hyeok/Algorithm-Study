import sys


def find_parent(parent, x):     # x와 연결된 가장 작은 숫자의 컴퓨터 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):        # 두 컴퓨터 연결하기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input_data = sys.stdin.readline
N = int(input_data())
M = int(input_data())
edge = []       # 컴퓨터를 연결하는 선
for _ in range(M):
    a, b, c = map(int, input_data().split())
    edge.append((c, a, b))
edge.sort()     # 비용 오름차순 정렬
parent = [0] * (N+1)
for i in range(N+1):
    parent[i] = i   # 부모를 자기 자신으로 초기화

result = 0
for i in range(M):
    cost, a, b = edge[i]
    if find_parent(parent, a) != find_parent(parent, b):    # 두 컴퓨터가 연결되어 있지 않다면
        union(parent, a, b)     # 연결
        result += cost

print(result)