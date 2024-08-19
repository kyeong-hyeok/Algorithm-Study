import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split(" "))
arr=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split(" "))

    arr[u].append(v)
    arr[v].append(u)

visited=[False for _ in range(n+1)]

def dfs(v):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)

cnt = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)    