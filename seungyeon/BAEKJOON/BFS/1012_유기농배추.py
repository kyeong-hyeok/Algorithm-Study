# # import sys
# # from collections import deque

# # input=sys.stdin.readline

# # dx=[-1,1,0,0]
# # dy=[0,0,1,-1]


# # def bfs(x,y):
# #     que = deque()
# #     que.append((x,y))

# #     cnt = 0

# #     while(que):

# #         x,y = que.popleft()
# #         for i in range(4):
# #             nx = x + dx[i]
# #             ny = y + dy[i]

# #             if nx < 0 or nx >= n or ny < 0 or ny >= m:
# #                 continue

# #             if arr[nx][ny] == 1:
# #                 arr[nx][ny] = 0
# #                 que.append((nx,ny))
# #                 cnt += 1

# #     return cnt

# # t = int(input())

# # for i in range(t):

# #     n,m,k = map(int,input().split())

# #     arr = [[0]*m for _ in range(n)]

# #     for j in range(k):
# #         x,y=map(int,input().split())
# #         arr[x][y] = 1

# #     cnt = 0
# #     for i in range(n):
# #         for j in range(m):
# #             if arr[i][j] == 1:
# #                 bfs(i,j)
# #                 cnt += 1
# #     print(cnt)

# import sys
# from collections import deque

# input=sys.stdin.readline

# dx=[-1,1,0,0]
# dy=[0,0,1,-1]


# def bfs(x,y):

#     que =deque()
#     que.append((x,y))

#     while (que):
#         x,y=que.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= m or ny >= n:
#                 continue
#             if arr[nx][ny] == 1:
#                 que.append((nx,ny))
#                 arr[nx][ny] = 0


    
# t=int(input())

# for i in range(t):
#     answer = 0
#     m,n,k=map(int,input().split(" "))

#     arr=[[0] * n for _ in range(m)]

#     for i in range(k):
#         x,y=map(int,input().split(" "))
#         arr[x][y] = 1

#     for a in range(m):
#         for b in range(n):
#             if arr[a][b] == 1:
#                 bfs(a,b)
#                 answer += 1

#     print(answer)

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):

    que=deque()

    que.append((x,y))

    while que: 
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx < 0 or ny < 0 or nx >= X or ny >= Y:
                continue

            if not visited[ny][nx] and (ny,nx) in q:
                visited[ny][nx] = True
                que.append((nx,ny))
            

    return 1


t = int(input().rstrip())

for _ in range(t):
    X,Y,K=map(int,input().split())

    q=deque()
    for i in range(K):
        x,y = map(int,input().split())
        q.append((y,x))

        # 한 묶음을 찾아야함
    
    visited=[[False for _ in range(X)] for _ in range(Y)]

    cnt = 0
    while q:
        y,x=q.popleft()

        if not visited[y][x]:
            cnt += bfs(x,y)
            # cnt +=1

    print(cnt)