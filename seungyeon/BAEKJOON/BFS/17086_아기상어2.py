import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())

dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,1,1,-1,-1]

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

que = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            que.append((i,j))

x,y,cnt=0,0,0

while que:
    x,y=que.popleft()

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx >= n or ny < 0 or ny >= m:
            continue

        if not arr[nx][ny] :
            arr[nx][ny] = arr[x][y] + 1
            que.append((nx,ny))
answer = 0
for a in arr:
    answer = max(answer,max(a))

print(answer-1)