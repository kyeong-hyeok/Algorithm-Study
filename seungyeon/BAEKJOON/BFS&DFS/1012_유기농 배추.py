import sys
from collections import deque
input = sys.stdin.readline
que=deque()
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(a,b):
    que.append((a,b))
    arr[a][b] = 0 # 방문처리

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny=y+dy[i]

            if nx < 0  or nx >= n or ny < 0 or ny >= m :
                continue

            if  arr[nx][ny] == 1:
                que.append((nx,ny))
                arr[nx][ny] = 0


t=int(input())
arr=[]
for i in range(t):
    m,n,k=map(int,input().split())
    arr=[[0] * m for _ in range(n)]
    answer = 0

    for j in range(k):
        x,y=map(int,input().split())
        arr[y][x] = 1
    
    for a in range(n):
        for b in range(m): 
            if arr[a][b] == 1:
                bfs(a,b)
                answer += 1

print(answer)




                




