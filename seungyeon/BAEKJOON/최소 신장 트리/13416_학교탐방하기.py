# 최적의 경우 : n
# 최악의 경우 : 0 -> 계속 +
import sys

input=sys.stdin.readline

n,m=map(int,input().split(" "))
arr=[]
for i in range(m+1):
    arr.append(tuple(map(int, input().split())))


def get_parent(x,parent):
    if x == parent[x]:
        return x
    return get_parent(parent[x],parent)

def union(x,y,parent):
    x = get_parent(x,parent)
    y = get_parent(y,parent)
    parent[max(x,y)] = min(x,y)

worst,best = 0,n

maxParent=[i for i in range(n+1)]
minParent=[i for i in range(n+1)]

for x,y,c in arr:

    if c == 1:
        x = get_parent(x,minParent)
        y = get_parent(y,minParent)

        if x != y:
            best -= 1
            union(x,y,minParent)

    else:
        x = get_parent(x,maxParent)
        y = get_parent(y,maxParent)

        if x != y:
            worst += 1
            union(x,y,maxParent)

print(worst**2 - best**2)

