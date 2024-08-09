from collections import deque

def bfs(start,find):
    que = deque()
    que.append((start,0))
    visited = [False] * (n+1)
    visited[start] = True

    while que:
        v,d = que.popleft()

        if v == find:
            return d
        
        for i,l in graph[v]:
            if not visited[i]:
                visited[i] = True
                que.append((i,d+l))


n,m=map(int,input().split(" "))

graph=[[]for i in range(n+1)]

for i in range(n-1):
    x,y,k=map(int,input().split())
    graph[x].append((y,k))
    graph[y].append((x,k))

for j in range(m):
    a,b=map(int,input().split(" "))
    print(bfs(a,b))

