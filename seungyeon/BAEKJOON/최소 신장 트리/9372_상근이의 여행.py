import sys,heapq
input = sys.stdin.readline


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

t = int(input())

for i in range(t):
    n,m=map(int,input().split())

    parent=[i for i in range(n+1)]
    arr=[]

    for j in range(m):
        a,b=map(int,input().split())
        arr.append((a,b))

    arr.sort()
    answer = 0
    
    for c,d in arr:
        if not same_parent(c,d):
            union_parent(c,d)
            answer += 1

    print(answer)
