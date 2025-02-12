# import sys
# from collections import deque
# input=sys.stdin.readline

# n,m=map(int,input().split(" "))
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().rstrip())))

# visited=[[[0] * 2 for _ in range(m)]]

# dx=[-1,1,0,0]
# dy=[0,0,1,-1]

# def bfs(x,y,z):

#     que=deque()
#     que.append((x,y,z))

#     while que:

#         if x == m-1 and y == n-1:
#             return visited[x][y][z]
        
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]

#             if nx < 0 or ny < 0 or nx >= m or ny >= n:
#                 continue


#             if arr[nx][ny] == 1 and z == 0 :
#                 visited[nx][ny][1] = visited[x][y][0] + 1
#                 que.append((nx,ny,1))
#             elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
#                 visited[nx][ny][z] = visited[x][y][z] + 1
#                 que.append((nx,ny,z))

#     return -1

# print((bfs(0,0,0)))

# import sys
# from collections import deque

# input=sys.stdin.readline

# n,m=map(int,input().split(" "))

# arr=[list(map(int,input().strip())) for _ in range(n)]


# dx=[-1,1,0,0]
# dy=[0,0,1,-1]


# def bfs(x,y):

#     arr[x][y] = 1
#     que=deque()
#     que.append((x,y))

#     while que:
#         x,y=que.popleft()

#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]

#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue

#             if arr[nx][ny] == 0:
#                 arr[nx][ny] = arr[x][y] + 1
#                 que.append((nx,ny))

#     return arr[n-1][m-1]

# answer = 222222

#  # 한개만 부셔서 최단거리 
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1:
#             arr[i][j] = 0 
#             answer = min(answer,bfs(0,0))
#             arr[i][j] = 1

# if answer == 0:
#     print(-1)
# else : print(answer)


import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split(" "))

visited=[[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


arr=[list(map(int,input().strip())) for _ in range(n)]


dx=[-1,1,0,0]
dy=[0,0,1,-1]


def bfs(x,y,z):

    que=deque()
    que.append((x,y,z))

    while que:
        x,y,z=que.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]
        

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if arr[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                que.append((nx,ny,1))

            elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z]+ 1
                que.append((nx,ny,z))


    return -1

print(bfs(0,0,0))
