# 같은수 여러번 가능

import sys
from itertools import combinations

input = sys.stdin.readline
n,m = map(int,input().split())

num = [i for i in range(1,n+1)]

visited=[False]*(n+1)
arr = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(1,n+1):
            arr.append(i)
            dfs(depth+1)
            arr.pop()

dfs(0)