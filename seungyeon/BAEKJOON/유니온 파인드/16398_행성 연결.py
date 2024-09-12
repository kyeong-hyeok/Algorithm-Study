import sys

input=sys.stdin.readline

n = int(input().rstrip())
parent=[k for k in range(n+1)]

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

    else:
        parent[a] = b

def is_same_parent(a,b):
    return get_parent(a) == get_parent(b)


arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

que=[]
for i in range(n):
  for j in range(0,i,1):
      que.append((arr[i][j],i+1,j+1))

que.sort()

sum = 0
for c,a,b in que:
    if not is_same_parent(a,b):
        union_parent(a,b)
        sum += c
print(sum)