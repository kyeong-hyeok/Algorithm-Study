

# import sys
# X,Y,H=map(int,input().split())
# arr=[[] for _ in range(H)]
# for i in range(H):
#     for j in range(Y):
#         arr[i].append(list(map(int,input().split())))


# dx=[-1,1,0,0,0,0]
# dy=[0,0,1,-1,0,0]
# dh=[0,0,0,0,-1,1]

# visited=[[[False for _ in range(X)] for _ in range(Y)] for _ in range(H)]
# from collections import deque

# que=deque()
# answer = 0

# def bfs():

#     while que:
#         h,y,x=que.popleft()

#         for k in range(6):
#             nh=h+dh[k]
#             nx=x+dx[k]
#             ny=y+dy[k]

#             if nx < 0 or ny < 0 or nh < 0 or nx >= X or ny >= Y or nh >= H:
#                 continue

#             if arr[nh][ny][nx] == 0 and not visited[nh][ny][nx]:
#                 que.append(((nh,ny,nx)))
#                 arr[nh][ny][nx] = arr[h][y][x] + 1
#                 visited[nh][ny][nx] = True

# for h in range(H):
#     for j in range(Y):
#         for i in range(X):
#             if not visited[h][j][i] and arr[h][j][i] == 1:
#                 que.append((h,j,i))
#                 visited[h][j][i] = True

# bfs()

# for a in arr:
#     for b in a:
#         for c in b:
#             if c == 0:
#                 print(-1)
#                 exit(0)

#         answer = max(answer,max(b))

# print(answer -1)
                    


import sys
from collections import deque

X,Y,H=map(int,input().split())

arr=[[ ] for _ in range(H)]
for h in range(H):
    for j in range(Y):
        arr[h].append(list(map(int,input().split())))


dx=[-1,1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dh=[0,0,0,0,-1,1]

que = deque()

visited=[[[False for _ in range(X)] for _ in range(Y)] for _ in range(H)]
def bfs():


    while que:
        h,y,x=que.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = h + dh[i]


            if nx < 0 or ny < 0 or nh < 0 or nx >= X or ny >= Y or nh >= H:
                continue

            if arr[nh][ny][nx] == 0 and not visited[nh][ny][nx]:
                que.append((nh,ny,nx))
                arr[nh][ny][nx] = arr[h][y][x] + 1
                visited[nh][ny][nx] = True



answer = 0
for i in range(H):
    for j in range(Y):
        for k in range(X):

            if arr[i][j][k] == 1 and not visited[i][j][k]:
                que.append((i,j,k))


bfs()


for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)

        answer = max(answer,max(j))

print(answer -1)


