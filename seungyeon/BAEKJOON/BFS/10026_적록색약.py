# # from collections import deque


# # def bfs(x,y):

# #     que.append((x,y))

# #     dx=[1,-1,0,0]
# #     dy=[0,0,-1,1]
# #     visited[x][y] = 1

# #     while(que):
        
# #         x,y = que.popleft()

# #         for i in range(4):
# #             nx = x + dx[i]
# #             ny = y + dy[i]

# #             if nx < 0 or nx >= n or ny < 0 or ny >= n:
# #                 continue

# #             if arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
# #                 visited[nx][ny] = 1
# #                 que.append((nx,ny))
            


# # n = int(input())
# # arr=[]
# # que = deque()

# # for i in range(n):
# #     arr.append(list(input().strip()))


# # visited=[[0]*n for _ in range(n)]
# # cnt1 = 0
# # for i in range(n):
# #     for j in range(n):
# #         if not visited[i][j]:
# #             bfs(i,j)
# #             cnt1 += 1

# # for i in range(n):
# #     for j in range(n):
# #         if arr[i][j] == 'G':
# #             arr[i][j] = 'R'

# # visited=[[0]*n for _ in range(n)]
# # cnt2 = 0
# # for i in range(n):
# #     for j in range(n):
# #         if not visited[i][j]:
# #             bfs(i,j)
# #             cnt2+=1

# # print(cnt1,cnt2)


# import sys
# from collections import deque
# input=sys.stdin.readline

# n = int(input())
# arr=[]
# for i in range(n):
#     arr.append(list(input().strip()))


# # 2번째에는 R -> G 로 하고 구역 개수 세기
# dx=[-1,1,0,0]
# dy=[0,0,1,-1]

# def bfs(x,y):

#     que=deque()

#     que.append((x,y))
#     visited[x][y] = 1

#     while que:
#         x,y=que.popleft()

#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]

#             if nx < 0 or ny < 0 or nx >=n or ny >=n:
#                 continue

#             if arr[nx][ny] == arr[x][y] and visited[nx][ny] == 0:
#                 que.append((nx,ny))
#                 visited[nx][ny] = 1

# visited = [[0] * n for i in range(n)]
# cnt1,cnt2= 0,0

# for i in range(n):
#     for j in range(n):
#         if not visited[i][j]:
#             bfs(i,j)
#             cnt1 += 1


# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == "R":
#             arr[i][j] = "G"

# visited = [[0] * n for i in range(n)]

# for i in range(n):
#     for j in range(n):
#         if not visited[i][j]:
#             bfs(i,j)
#             cnt2 += 1

   
# print(cnt1,cnt2)

# 적록색약이 아닌사람의 구역의 개수, 적록색약이 사람이 봤을 떄 구역의 개수 
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(input().strip()))


dx=[-1,1,0,0]
dy=[0,0,1,-1]

visited=[[False] * n for i in range(n)]

from collections import deque

def bfs(x,y):
    que=deque()
    que.append((x,y))

    visited[x][y] = True

    while que:
        x,y= que.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx < 0 or ny < 0 or nx >=n or ny >= n :
                continue

            if not visited[nx][ny] and arr[x][y] == arr[nx][ny]:
                visited[nx][ny] = True
                que.append((nx,ny))

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1

# 적록색약
for i in range(n):
    for j in range(n):
        visited[i][j] = False

        if arr[i][j] == "R":
            arr[i][j] = "G"

cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt,cnt2)