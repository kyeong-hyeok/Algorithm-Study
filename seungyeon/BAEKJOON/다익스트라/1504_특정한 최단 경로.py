import heapq
import sys

input=sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
graph = [[] for i in range(v+1)]

for _ in range(e):
    x,y,c=map(int,input().split())
    graph[x].append((y,c))
    graph[y].append((x,c))


def dijkstra(start):
    distance=[INF]*(v+1)
    que=[]
    heapq.heappush(que,(0,start))
    distance[start] = 0

    while que:
        dist,new=heapq.heappop(que)

        if distance[new] < dist:
            continue

        for a,b in graph[new]:

            cost=dist+b

            if distance[a] > cost:
                distance[a]  = cost
                heapq.heappush(que,(cost,a)) # 비용별 정렬

    return distance

v1,v2=map(int,input().split())

original=dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist=dijkstra(v2)

v1_sum = original[v1] + v1_dist[v2] + v2_dist[v]
v2_sum=original[v2]+v2_dist[v1]+v1_dist[v]

answer=min(v1_sum,v2_sum)
print(answer if answer < INF else -1)