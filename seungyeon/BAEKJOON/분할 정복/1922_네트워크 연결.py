# 모든 컴퓨터를 연결하는데 필요한 최소 비용 : 크루스칼 알고리즘
# 모든 간선에 대해 정렬한 후 가장 거리가 짧은 것 부터 집합에 포함
# 사이클 발생하지 않는지(같은 집합인지) 확인하면서 연결해야함.\

def find(a): # 부모노드 찾기 
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if b < a: # 2) 합치려면(find) 작은 부모가 루트노드가 되도록. 부모 노드로 연결 ex ) arr[3] = 2
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())
arr = []
parent = [i for i in range(n+1)] # 1) 초기 설정 : 각 노드의 루트노드를 자기 자신
answer = 0
for i in range(m):
    a,b,c = map(int,input().split())
    arr.append((c,a,b))
arr.sort(key=lambda x:x[0]) # x[0] 기준으로 정렬

for c,a,b in arr:
    if find(a) != find(b): # 같은 집합에 속하지 않는다면
        union(a,b) # 합치기
        answer += c
print(answer)
