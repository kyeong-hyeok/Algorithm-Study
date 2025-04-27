import sys
import heapq
input=sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())


INF=sys.maxsize

dp=[INF] * (n+1)
prev_node=[0] * (n+1)

heap = []
arr=[[] for _ in range(n+1)]
answer = []

for i in range(m):
    s,e,w = map(int,input().split())

    arr[s].append((w,e))

def dij(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while(heap):
        now_weight,now_end = heapq.heappop(heap)

        if dp[now_end] < now_weight:
            continue

        for new_weight,new_node in arr[now_end]:
            next_weight = now_weight + new_weight

            if next_weight < dp[new_node]:
                dp[new_node] = next_weight
                prev_node[new_node] = now_end
                heapq.heappush(heap,(next_weight,new_node))


start,end=map(int,input().split())


dij(start)

print(dp[end])

answer=[end]
now = end
while(now != start):
    now = prev_node[now]
    answer.append(now)
answer.reverse()
print(len(answer)) # 경로 개수 
print(*answer) # 경로


# arr=[[] for i in range(n+1)]
# for i in range(m):
#     s,e,w = map(int,input().split())

#     arr[s].append((w,e))

# arr.sort(key= lambda x : x[0])

# start,end=map(int,input().split())

# answer=[]
# weight=sys.maxsize
# visited=[False   for _ in range(n+1)]

# def sol(k):

#     for new_weight,new_end in arr[k]:
#         if new_end == end:
#             return answer
        
#         if new_weight < weight:
#             weight = new_weight
#             answer.pop
#             answer.append(new_end)
#             visited[new_end] = True
#             sol(new_end)


# sol(start)
# print(weight)
# print(len(answer))
# print(*answer)