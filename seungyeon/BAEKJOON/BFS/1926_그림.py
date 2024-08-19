# import sys
# from collections import deque
# input=sys.stdin.readline


# n,m=map(int,input().split())
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().split())))

# que=deque()



# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(arr,i,j):
#     que=deque()
#     que.append((i,j))
#     arr[i][j] = 0
#     cnt = 1


#     while(que):
#         x,y = que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx<0 or nx >= n or ny < 0 or ny >= m:
#                 continue

#             if arr[nx][ny] == 1:
#                 arr[nx][ny] = 0
#                 que.append((nx,ny))
#                 cnt += 1
#     return cnt

# answer = []

# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1:
#             answer.append(bfs(arr,i,j))

# if len(answer) == 0:
#     print(len(answer))
#     print(0)
# else:
#     print(len(answer))
#     print(max(answer))


import sys
from collections import deque
input =  sys.stdin.readline

n, m = map(int, input().split(' '))
arr = []

for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

que=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    cnt = 1

    que=deque()
    que.append((x,y))

    arr[x][y] = 0

    while(que):

        x ,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                que.append((nx,ny))
                cnt += 1

    return cnt

answer=[]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            answer.append(bfs(i,j))

if len(answer) == 0:
    print(0)
    print(0)
else :
    print(len(answer))
    print(max(answer))
