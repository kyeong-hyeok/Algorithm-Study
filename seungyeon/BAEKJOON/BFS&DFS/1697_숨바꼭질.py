import sys
from collections import deque

input=sys.stdin.readline

def bfs(v): # dfs로 가장 깊은 노드까지 가는건 시간 낭비 bfs로 빨리 찾는게 
    que = deque([v])
    while que:
        v = que.popleft()
        if v == k:
            return arr[v]
        
        for next in (v-1,v+1,2*v):
            if 0<=next < MAX and not arr[next]:
                arr[next] = arr[v]+1
                que.append(next)


MAX = 100001
n,k=map(int,input().split())
arr = [0] * MAX

print(bfs(n))