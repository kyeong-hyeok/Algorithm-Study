# import sys
# input=sys.stdin.readline

# def dfs(x):
#     visited[x] = True # 방문
#     a = arr[x] # 1 -> 3 -> 3 -> 7 
#     if not visited[a]:
#         dfs(a)

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     arr = [0] + list(map(int,input().split()))
#     visited = [False]* (n+1)
#     result = 0

#     for i in range(1,n+1):
#         if not visited[i]:
#             dfs(i)
#             result += 1
#     print(result)



def dfs(x):
    visited[x] = True
    a = arr[x]
    if not visited[a]:
        dfs(a)

t = int(input())

for i in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visited=[False]*(n+1)
    result = 0

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
            result += 1

    print(result)