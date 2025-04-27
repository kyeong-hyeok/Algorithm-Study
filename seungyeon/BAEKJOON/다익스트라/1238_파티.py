import sys
from collections import deque
import heapq

input=sys.stdin.readline

n,m,x=map(int,input().split())
INF=int(1e9)
arr=[[INF]*(n+1)  for i in range(n+1)]

arr=[[] for i in range(n+1)]
arr_reverse=[[] for i in range(n+1)]

for i in range(m):
    x,y,c=map(int,input().split())

    arr[x].append((y,c))
    arr_reverse[y].append((x,c))


def dijk(start,arr):
    distance=[INF] * (n+1)

    que=[]
    heapq.heappush(que,(0,start))
    distance[start] = 0

    while(que):
        dist,new=heapq.heappop(que)

        if distance[new] < dist:
            continue

        for a,b in arr[new]:

            cost = dist+b

            if distance[a] > cost:
                distance[a] = cost
                heapq.heappush(que,(cost,a))

    return distance


# start_distance=dijk[x]

total_dist=[]
total_dist.append([])
for i in range(1,n+1):
    total_dist.append(dijk(i,arr))

tmp = 0
for j in range(1,n):
    tmp = max(tmp,total_dist[j][x] + total_dist[x][j])


print(tmp)

