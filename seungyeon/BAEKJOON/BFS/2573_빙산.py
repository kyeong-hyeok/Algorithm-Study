

from collections import deque

Y,X=map(int,input().split())

arr=[]
for i in range(Y):
    arr.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,1,-1]


# 주변 노드 탐색하며 녹일 숫자 세기기
def melt(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= Y or ny >= X:
            continue

        if arr[nx][ny] == 0:
            arr_around[x][y] += 1
        
# 한번에 녹여야함


def bfs(x,y):

    global tmp

    que=deque()
    que.append((x,y))

    tmp += 1
    
    while que:
        x,y=que.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx < 0 or ny < 0 or nx >= Y or ny >= X:
                continue
            if not visited[nx][ny] and arr[nx][ny] > 0:
                visited[nx][ny] = True
                que.append((nx,ny))

arr_around=[[0 for _ in range(X)] for _ in range(Y)]

year = 0
while True:

    year += 1
    check=0
    cnt = 0
    tmp = 0
    visited=[[False for _ in range(X)] for _ in range(Y)]

    que=deque()
    for i in range(Y):
        for j in range(X):
            if arr[i][j] > 0:
                que.append((i,j))
                melt(i,j)
                cnt += 1
    
    if cnt == 0:
        print(0)
        break

    for i in range(Y):
        for j in range(X):
            if arr[i][j] > arr_around[i][j]:
                arr[i][j] -= arr_around[i][j]
                arr_around[i][j] = 0
            else :
                arr[i][j] = 0
                arr_around[i][j] = 0


    for i in range(Y):
        for j in range(X):
            if arr[i][j] > 0 and not visited[i][j] :
                bfs(i,j)
    
    if tmp > 1:
        print(year)
        break

