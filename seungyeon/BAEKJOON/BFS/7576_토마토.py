# 같이 토마토 익히기를 진행해야함.
# 앞에있는 노드( (i,j)가 작다고 먼저 진행해서 덮어쓰면 안됨

# bfs 돌리기 전 que 에 넣어둘 때 
# [[1, -1, 7, 6, 5, 4],
#  [2, -1, 6, 5, 4, 3],
#  [3, 4, 5, 6, -1, 2], 
# [4, 5, 6, 7, -1, 1]]
# bfs 돌리면서 que 에 넣을 떄 
# [[1, -1, 7, 8, 9, 10],
#  [2, -1, 6, 7, 8, 9],
#  [3, 4, 5, 6, -1, 10],
#  [4, 5, 6, 7, -1, 1]]

import sys
from collections import deque
input=sys.stdin.readline

m,n = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

que = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            que.append((i,j))

def bfs():

    while(que):

        x,y = que.popleft()

        dx=[-1,1,0,0]
        dy=[0,0,-1,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    

            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                que.append((nx,ny))


bfs()
res = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    else:
        res  = max(res,max(i))

print(res - 1)


# import sys
# from collections import deque
# input=sys.stdin.readline

# m,n = map(int,input().split())
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().split())))

# dx=[-1,1,0,0]
# dy=[0,0,-1,1]

# def bfs(x,y):
#     que = deque()
#     que.append((x,y))

#     while(que):

#         x,y = que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
        
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue

#             if arr[nx][ny] == 0:
#                 arr[nx][ny] = arr[x][y] + 1
#                 que.append((nx,ny))

# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1:
#             bfs(i,j)
#             print(arr)

# res= 0
# for i in arr:
#     for j in i:
#         if j == 0:
#             print(-1)
#             exit(0)

#     res  = max(res,max(i))

# print(res - 1)
