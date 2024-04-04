import sys
from collections import deque  

input=sys.stdin.readline

f,s,g,u,d=map(int,input().split())

visited=[0]*(f+1)

def bfs():

    que = deque()
    que.append(s)
    
    visited[s] = 1

    while que:
        y = que.popleft()

        if y == g:
            return visited[y] -1
        
        else:
            for dy in (y+u,y-d):
                if (0 < dy <= f) and visited[dy] == 0:
                    visited[dy] = visited[y] + 1
                    que.append(dy)

    return "use the stairs"
    
print(bfs())