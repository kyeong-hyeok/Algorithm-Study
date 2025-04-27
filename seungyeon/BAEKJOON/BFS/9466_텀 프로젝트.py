# t=int(input())
# from collections import deque
# import sys
# sys.setrecursionlimit(999999)

# def dfs(x):

#     global answer
#     visited[x] = True
#     cycle_list.append(x)
#     a = arr[x]

#     if visited[a] == True:
#         if a in cycle_list:
#            answer -= len(cycle_list[cycle_list.index(a):])
#         return
         
#     else:
#        dfs(a)


# for _ in range(t):

#     n=int(input())
#     answer = n

#     arr=[0]+list(map(int,input().split()))
#     visited= [False] * (n+1)

#     for i in range(1,n+1):
#         if not visited[i]:
#             cycle_list=[]
#             dfs(i)
        
#     print(answer)

# # dfs로 사이클 찾기 
# # 방문 유무로 사이클 생겼는지 찾기 
import sys
sys.setrecursionlimit(999999)


def dfs(x):

    global answer 
    visited[x] = True
    cycle.append(x)

    if visited[arr[x]]:
        if arr[x] in cycle:
            answer -= len(cycle[cycle.index[arr[x]]:])
        return 
    else:
        dfs(arr[x])



    if not visited[i]:


        dfs(arr[x])


t=int(input())
for _ in range(t):

    n=int(input())
    arr=[0]+list(map(int,input().split()))

    answer = n
    visited=[False] * (n+1)

    for i in range(1,n+1):
        if not visited[i]:
            cycle=[]
            dfs(i)

