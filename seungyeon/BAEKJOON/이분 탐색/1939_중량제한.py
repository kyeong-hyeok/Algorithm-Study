import sys
sys=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())

arr=[[] for i in range(n+1)] # 같은 노드에 여러개 다리 가능

for i in range(m):
    a,b,c=map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c)) # 도착노드, 가중치

a,b=map(int,input().split())

start,end=1,1000000000

result=0

# a부터 b까지 weight 의 가중치로 갈 수 있는지 여부 
def bfs(weight):
    que=deque()
    que.append(a)

    visited=[False]*(n+1)
    visited[a] = True

    while que:
        x = que.popleft()

        for i,w in arr[x]:
            if not visited[i] and w >= weight: # 해당 가중치를 통과해야함함
                visited[i] = True
                que.append(i)

    if visited[b]: return True
    else: return False


while start <= end:
    mid = (start+end)//2

    if bfs(mid):
        result=mid
        start = mid + 1

    else:
        end = mid - 1
print(result)
