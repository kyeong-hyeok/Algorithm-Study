# 상하좌우, 최단거리 -> BFS?
# 이웃한 육지로 이동 가능, 최단거리이지만 가장 긴 시간 

from collections import deque

n,m = map(int,input().split())
arr = [list((input())) for _ in range(n)]


dx = [1,-1,0,0]
dy= [0,0,1,-1]

def bfs(i,j):
    que = deque()
    que.append((i,j))

    visited=[[0]*m for _ in range(n)]
    visited[i][j] = 1
    time = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >= n or ny <0 or ny >= m:
                continue
            elif arr[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                time = max(time,visited[nx][ny]) # 가장 긴 시간 
                que.append((nx,ny))
    return time -1

answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            answer = max(answer,bfs(i,j))
print(answer)