import sys
from collections import deque
input=sys.stdin.readline


n=int(input())
m=int(input())
arr=[[0] *(n+1) for i in range(n+1)]
visited=[0] * (n+1)

for i in range(m):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(k):
    que = deque()
    visited[k] = 1
    que.append(k)

    while que:
        a = que.popleft()
        for i in arr[a]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = visited[a] + 1
                
bfs(1)
answer = 0
for i in range(2,n+1):
     if visited[i] < 4 and visited[i] != 0:
         answer += 1
print(answer)
            
    

# import sys
# from collections import deque
# input=sys.stdin.readline


# n=int(input())
# m=int(input())
# arr=[[0 for j in range(n+1)] for i in range(n+1)]
# visited=[0] * (n+1)

# for i in range(m):
#     x,y=map(int,input().split())
#     arr[x][y] = 1
#     arr[y][x] = 1

# def bfs(k,depth):

#     #if depth==2:
#           #  print("here")
#            # return
    
#     que = deque()
#     que.append(k)
#     visited[k] = 1
    
#     while que:
        
#         top = que.popleft()
#         for i in range(n):
#             if arr[top][i] == 1 and  visited[i] == 0 :
#                 visited[i] = visited[top] + 1
#                 que.append(i)
                
# bfs(1,0)
# answer = 0
# for i in visited:
#      if i > 1 and i < 4:
#           answer += 1
# print(answer)