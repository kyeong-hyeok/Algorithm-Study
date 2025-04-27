# # # # 최대 몇개 


# # import sys
# # from collections import deque
# # input=sys.stdin.readline
# # sys.setrecursionlimit(100000)

# # arr=[]
# # n=int(input())

# # for i in range(n):
# #     arr.append(list(map(int,input().split())))


# # dx=[-1,1,0,0]
# # dy=[0,0,1,-1]

# # def dfs(x,y,h):
    
# #     for i in range(4):
# #         nx = x + dx[i]
# #         ny = y + dy[i]

# #         if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > h :
# #             dfs(nx,ny,h)

# # answer  = 1

# # for k in range(max(map(max,arr))):
# #     water = [[0]* n for _ in range(n)]
# #     cnt = 0
# #     for i in range(n):
# #         for j in range(n):
# #             if arr[i][j] > k and water[i][j] == 0:
# #                 cnt += 1
# #                 water[i][j] = 1
# #                 dfs[i][j] = 1
# #     answer = max(answer,cnt)

# # print(answer)

# # # import sys
# # # from collections import deque
# # # input=sys.stdin.readline

# # # arr=[]
# # # n=int(input())

# # # for i in range(n):
# # #     arr.append(list(map(int,input().split())))

# # # water=[[0 for i in range(n)] for i in range(n)]

# # # def rotate(k):
# # #     for i in range(n):
# # #         for j in range(n):
# # #             if arr[i][j] - k <= 0 :
# # #                 water[i][j] = 0
# # #             else:
# # #                 water[i][j]=1
# # #                 bfs(i,j)

# # # dx=[-1,1.0,0]
# # # dy=[0,0,1,-1]

# # # def bfs(x,y):
# # #     que = deque()
# # #     que.append((x,y))

# # #     while(que):

# # #         x,y=que.popleft

# # #         for i in range(4):
# # #             nx = x + dx[i]
# # #             ny = y + dy[i]

# # #             if nx < 0 or nx <= n or ny < 0 or ny <= n:
# # #                 continue
# # #             if water[nx][ny] == 1:
# # #                 que.append(nx,ny)
# # #                 water[nx][ny] = 0
                

# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(100000)

# n = int(input().rstrip())

# arr=[]
# for _ in range(n):
#     arr.append(list(map(int,input().split())))

# def dfs(x,y,k):
#     dx=[-1,1,0,0]
#     dy=[0,0,1,-1]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y+ dy[i]

#         if (0 <= nx < n) and (0 <= ny < n) and water[nx][ny] == 0 and arr[nx][ny] > k:
#             water[nx][ny] = 1
#             dfs(nx,ny,k)

# answer = 1

# for k in range(max(map(max,arr))):
#     water=[[0] * n for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] > k and not water[i][j]:
#                 cnt += 1
#                 water[i][j] = 1
#                 dfs(i,j, k)
#     answer = max(answer,cnt)

# print(answer)


import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

n=int(input())


arr=[list(map(int,input().split())) for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dfs(x,y,h):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if arr[nx][ny] > h and visited[nx][ny] == 0:
            visited[nx][ny] = True
            dfs(nx,ny,h)


answer = 1
for h in range(max(map(max,arr))):
    visited=[[False]*n for i in range(n)]

    cnt = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(i,j,h)
    
    answer = max(answer,cnt)


print(answer)