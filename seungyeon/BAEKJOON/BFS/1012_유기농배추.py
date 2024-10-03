# import sys
# from collections import deque

# input=sys.stdin.readline

# dx=[-1,1,0,0]
# dy=[0,0,1,-1]


# def bfs(x,y):
#     que = deque()
#     que.append((x,y))

#     cnt = 0

#     while(que):

#         x,y = que.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue

#             if arr[nx][ny] == 1:
#                 arr[nx][ny] = 0
#                 que.append((nx,ny))
#                 cnt += 1

#     return cnt

# t = int(input())

# for i in range(t):

#     n,m,k = map(int,input().split())

#     arr = [[0]*m for _ in range(n)]

#     for j in range(k):
#         x,y=map(int,input().split())
#         arr[x][y] = 1

#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 1:
#                 bfs(i,j)
#                 cnt += 1
#     print(cnt)

import sys
from collections import deque

input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,1,-1]


def bfs(x,y):

    que =deque()
    que.append((x,y))

    while (que):
        x,y=que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if arr[nx][ny] == 1:
                que.append((nx,ny))
                arr[nx][ny] = 0


    
t=int(input())

for i in range(t):
    answer = 0
    m,n,k=map(int,input().split(" "))

    arr=[[0] * n for _ in range(m)]

    for i in range(k):
        x,y=map(int,input().split(" "))
        arr[x][y] = 1

    for a in range(m):
        for b in range(n):
            if arr[a][b] == 1:
                bfs(a,b)
                answer += 1

    print(answer)