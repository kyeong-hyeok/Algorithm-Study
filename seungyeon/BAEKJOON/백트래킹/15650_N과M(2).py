import sys
from itertools import combinations

input = sys.stdin.readline
n,m = map(int,input().split())

num = [i for i in range(1,n+1)]


# for i in combinations(num,m):
#     print(*i)


visited=[False]*(n+1)
arr = []

def dfs(depth):
    if depth == m:
        print(''.join(map(str,arr)))
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(depth+1)
            visited[i] = False
            arr.pop()

dfs(0)