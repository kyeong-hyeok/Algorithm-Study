

# import sys,heapq
# INF = sys.maxsize
# input=sys.stdin.readline

# V,E=map(int,input().split(" "))
# k = int(input())


# dp=[INF] * (V+1)
# heap = []
# arr=[[] for _ in range(V+1)]

    
# # k ~ i 까지 최단경로 경로값. 시작점 자신은 0으로 출력, 경로가 없으면 INF

# def dij(start):
#     dp[start] = 0 # 가중치 테이블 dp 에서 시작 정점의 가중치 0으로 초기화
#     heapq.heappush(heap,(0,start)) # 시작 정점 (가중치,정점) 힙에 추가

#     while heap:
#         weight,now = heapq.heappop(heap) # 가장 가중치가 작은 정점(가중치,정점)

#         # 현재 테이블과 비교해서 가중치가 더 크다면 무시
#         if dp[now] < weight:
#             continue

#         for w,next_node in arr[now]: # 지금 정점과 연결된 다음 정점
#             next_weight = weight + w 

#             if next_weight < dp[next_node]: # 다음 가중치 합이 작으면 갱신
#                 dp[next_node] = next_weight

#                 heapq.heappush(heap,(next_weight,next_node)) # 그 노드를 heap 에 


# for _ in range(E):
#     u,v,w=map(int,input().split(" "))
#     arr[u].append((w,v))

# dij(k)


# for i in range(1,V+1):
#     if dp[i] == INF:
#         print("INF")
#     else:
#         print(dp[i])



import sys,heapq
INF = sys.maxsize
input=sys.stdin.readline

V,E=map(int,input().split(" "))
k = int(input())


dp=[INF] * (V+1)
heap = []
arr=[[] for _ in range(V+1)]

    
# k ~ i 까지 최단경로 경로값. 시작점 자신은 0으로 출력, 경로가 없으면 INF

def dij(start):
    dp[start] = 0 # 가중치 테이블 dp 에서 시작 정점의 가중치 0으로 초기화
    heapq.heappush(heap,(0,start)) # 시작 정점 (가중치,정점) 힙에 추가

    while heap:
        weight,now = heapq.heappop(heap) # 가장 가중치가 작은 정점(가중치,정점)

        # 현재 테이블과 비교해서 가중치가 더 크다면 무시
        if dp[now] < weight:
            continue

        for w,next_node in arr[now]: # 지금 정점과 연결된 다음 정점
            next_weight = weight + w 

            if next_weight < dp[next_node]: # 다음 가중치 합이 작으면 갱신
                dp[next_node] = next_weight

                heapq.heappush(heap,(next_weight,next_node)) # 그 노드를 heap 에 


for _ in range(E):
    u,v,w=map(int,input().split(" "))
    arr[u].append((w,v))

dij(k)


for i in range(1,V+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])

