import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split(" "))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().rstrip())))

visited=[[[0] * 2 for _ in range(m)]]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,z):

    que=deque()
    que.append((x,y,z))

    while que:

        if x == m-1 and y == n-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue


            if arr[nx][ny] == 1 and z == 0 :
                visited[nx][ny][1] = visited[x][y][0] + 1
                que.append((nx,ny,1))
            elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                que.append((nx,ny,z))

    return -1

print((bfs(0,0,0)))