from collections import deque


def bfs(x,y):

    que.append((x,y))

    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    visited[x][y] = 1

    while(que):
        
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                que.append((nx,ny))
            


n = int(input())
arr=[]
que = deque()

for i in range(n):
    arr.append(list(input().strip()))


visited=[[0]*n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited=[[0]*n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2+=1

print(cnt1,cnt2)


