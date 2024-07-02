import sys
from collections import deque
input=sys.stdin.readline


    
def bfs(x,y):


    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    que = deque()

    que.append((x,y))


    while(que):
        x,y = que.popleft()

        if x == goalX and y == goalY:
            return arr[x][y] 

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= k or ny < 0 or ny >= k:
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1 
                que.append((nx,ny))


t =int(input())

for i in range(t):
    k = int(input())
    currX,currY = map(int,input().split())
    goalX,goalY = map(int,input().split())
    arr = [[0]*k for _ in range(k)]
    print(bfs(currX,currY))
