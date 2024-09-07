import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
arr=[[] for _ in range(n+1)]
visited=[ False ] * (n+1)
for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0

def dfs(depth,x):

    global cnt 

    if depth > 1:
        return 
    
    if not visited[x]:
        visited[x] = True
        cnt += 1 
        
    for i in arr[x]:
        if not visited[i]:
          dfs(depth+1,i)
                
visited[1] = True
for i in arr[1]:
    dfs(0,i)

print(cnt)

# def bfs(x):

#     que=deque()

#     que.append(x)
#     cnt = 1

#     while(que):

#         x = que.popleft()
#         if not visited[x]:
#             visited[x] = True

#         for i in arr[x]:
#             if not visited[i]:
#                 visited[i] = True
#                 que.append(i)
#                 cnt += 1

#     return cnt 
    

# # print(bfs(1))
