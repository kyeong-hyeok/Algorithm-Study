import sys
input=sys.stdin.readline



def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def is_same_parent(a,b):
    return get_parent(a) == get_parent(b)

t=int(input())

for i in range(t):
    n = int(input())
    arr=list(map(int,input().split()))
    graph=[]
    for i in range(1,n+1):
        graph.append((i,arr[i-1]))

    parent=[i for i in range(n+1)]


    answer = 0
    for a,b in graph:
        if not is_same_parent(a,b):
            union_parent(a,b)
            answer += 1


    print(n-answer)   
