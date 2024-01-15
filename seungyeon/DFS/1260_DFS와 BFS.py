import sys
from collections import deque
input=sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = True # 방문처리
    while q :
        v = q.popleft()
        print(v,end=" ")
        for i in range(1,n+1):
            if not visited[i] and arr[v][i]: # 방문하지 않았고, 간선이 있을 때
                q.append(i)
                visited[i] = True

def dfs(v):
    visited[v] = True
    print(v,end=" ")
    for i in range(1,n+1):
        if not visited[i] and arr[v][i]:
            dfs(i)

n,m,v = map(int,input().split())
arr = [[False]*(n+1)  for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    arr[a][b] = True
    arr[b][a] = True

visited = [False] * (n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)
