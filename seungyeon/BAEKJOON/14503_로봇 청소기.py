import sys
input=sys.stdin.readline
dr=[-1,0,1,0]
dc=[0,1,0,-1]

n,m=map(int,input().split())
r,c,d=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

visited=[[0] * m for _ in range(n)]
visited[r][c] = 1 # 출발지

answer = 1
while True:
    check = False

    for i in range(4):
        d = (d + 3)  % 4

        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                check = True
                answer += 1
                r = nr
                c = nc
                break

    if not check:

        if arr[r-dr[d]][c-dc[d]] == 1:
            print(answer)
            break
        else:
            r,c = r-dr[d],c-dc[d]


# import sys
# input=sys.stdin.readline
# from collections import deque

# n,m=map(int,input().split())
# r,c,d=map(int,input().split())
# arr=[]

# for i in range(n):
#     arr.append(list(map(int,input().split())))

# dx=[-1,1,0,0]
# dy=[0,0,-1,1]

# compass = [[0,1],[1,0],[0,-1],[-1,0]]
# direct=[[1,0],[0,1],[-1,0],[0,-1]]

# def dfs():

#     answer =0

#     que = deque()
#     que.append((r,c))
#     while que:
#         x,y=que.popleft()

#         check=False
        
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]

#             if 0 > nx or nx > n or 0 > ny or ny >  m:
#                 print(nx,ny,'here??')
#                 continue

#             if (0 <= nx < n) and (0 <= ny < m) and arr[nx][ny] == 1: # 주변에 청소되지 않은 칸이 있는경우
#                 print("here")
#                 que.append((nx,ny))
#                 arr[nx][ny] = 0
#                 answer += 1
#                 check=True

#         if not check:
#             print("hihi")
#             x+=compass[d][0]
#             y+=compass[d][1]
#             que.append((x,y))
        
#     return answer
            
# print(dfs())
