# import sys
# from collections import deque


# n = int(input())
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input())))

# answer = []
# dx=[1,-1,0,0]
# dy=[0,0,1,-1]

# def bfs(x,y):
#     que = deque()
#     cnt = 1

#     que.append((x,y))

#     while(que):
#         x,y = que.popleft()
#         arr[x][y] = 0

#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]

#             if 0<= nx < n and 0<= ny < n and arr[nx][ny] == 1:
#                 que.append((nx,ny))
#                 cnt += 1
#                 arr[nx][ny] = 0

#     answer.append(cnt)

# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1:
#             bfs(i,j)

# print(len(answer))
# answer.sort()
# for i in answer:
#     print(i)

import sys
from collections import deque

input=sys.stdin.readline

n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().rstrip())))


dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    que=deque()

    que.append((x,y))
    arr[x][y] = 0
    cnt = 1
    
    
    while(que):
        x,y=que.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                que.append((nx,ny))
                cnt += 1
    return cnt


answer = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            answer.append(bfs(i,j))

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])