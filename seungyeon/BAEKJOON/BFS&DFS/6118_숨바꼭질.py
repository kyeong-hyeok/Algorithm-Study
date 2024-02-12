import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[]  for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

visitied=[0]* (n+1)

def bfs(v):

    que = deque()
    que.append(v)
    visitied[v] = 1
    while que:
        v = que.popleft()
        for i in arr[v]:
            if visitied[i] == 0 :
                visitied[i] = visitied[v] + 1
                que.append(i)
    
bfs(1)
answer = max(visitied)
print(visitied.index(answer),answer -1 , visitied.count(answer))
