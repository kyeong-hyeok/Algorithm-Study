# from collections import deque


# n,m=map(int,input().split())
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input())))


# dx = [-1,1,0,0]
# dy = [0,0,1,-1]

# def bfs(x,y):
#     que = deque()
#     que.append((x,y))

#     while(que):

#         x,y = que.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx >= n or ny >= m or nx < 0 or ny < 0:
#                 continue

#             if arr[nx][ny] == 0:
#                 continue

#             if arr[nx][ny] == 1:
#                 que.append((nx,ny))
#                 arr[nx][ny] = arr[x][y] + 1

#     return arr[n-1][m-1]


# print(bfs(0,0))

import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    que=deque()
    que.append((x,y))

    while que:
        x,y=que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1 # 그래프 값을 사용하기
                que.append((nx,ny))

    return arr[n-1][m-1]

print(bfs(0,0))
