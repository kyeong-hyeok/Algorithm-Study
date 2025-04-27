import sys
from collections import deque
Y,X,K=map(int,input().split())

arr=[[0 for _ in range(X)] for _ in range(Y)]

visited=[[False for _ in range(X)] for _ in range(Y)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
def bfs(x,y):

    cnt = 1
    que=deque()
    que.append((x,y))
    visited[y][x] = True

    while que:
        x,y=que.popleft()


        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                continue

            if arr[ny][nx] == 0 and not visited[ny][nx]:
                que.append((nx,ny))
                visited[ny][nx] = True
                cnt += 1

    return cnt



for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1

answer=[]
cnt = 0
for i in range(Y):
    for j in range(X):
        if arr[i][j] == 0 and not visited[i][j]:
            answer.append(bfs(j,i))
            visited[i][j] = True
            cnt += 1

print(cnt)
answer.sort()
for k in answer:
    print(k,end=' ')


