
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
m=int(input())

arr=[ [ ]for i in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

answer_dfs = 0
def dfs(k):

    global answer_dfs
    visited[k]= True
    
    for i in arr[k]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            answer_dfs+=1

dfs(1)
print(answer_dfs)



# def bfs(k):

#     answer = 0
#     que = deque()

#     que.append(k)

#     while que:
#         a = que.popleft()
#         visited[a] = True

#         for i in arr[a]:
#             if not visited[i]:
#                 que.append(i)
#                 visited[i] = True
#                 answer += 1

#     return answer

# print(bfs(1))

# def get_parent(x):
#     if parent[x] == x:
#         return x
#     parent[x] = get_parent(x)
#     return parent[x]

# def union_parent(a,b):
#     a = get_parent(a)
#     b = get_parent(b)

#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b


# def is_same_parent(a,b):
#     return get_parent(a) == get_parent(b)

# answer = 0
# # 연결을 해두고 정점 순회하면서 union 하고 개수 세기    
# for a,b in arr:
#     if not is_same_parent(a,b):
#         union_parent(a,b)
#         answer += 1
# print(answer)

# import sys
# from collections import deque
# input=sys.stdin.readline

# n=int(input())
# m=int(input())

# arr=[ [ ]for i in range(n+1)] # 리스트 컴프리헨션
# visited=[False]*(n+1)

# for i in range(m):
#     a,b=map(int,input().split())
#     arr[a].append(b)
#     arr[b].append(a)


# def bfs(k):

#     answer = 0
#     que = deque()

#     que.append(k)

#     while que:
#         a = que.popleft()
#         visited[a] = True # 이거 안써서 틀렸었음

#         for i in arr[a]:
#             if not visited[i]:
#                 que.append(i)
#                 visited[i] = True
#                 answer += 1

#     return answer

# print(bfs(1))

