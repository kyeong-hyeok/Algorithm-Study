import sys
import heapq
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort()

que = []
heapq.heappush(que,arr[0][1]) # 가장 빨리 끝나는 시간으로 초기화

for i in range(1,n):
    if arr[i][0] < que[0]: # 시작하는 시간이 가장 빨리 끝나는 시간보다 작다면 ( 수업 끝나고 진행할 수 없음 -> 강의실 추가(heappush))
        heapq.heappush(que,arr[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que,arr[i][1])

print(len(que))

# 그냥 큐 쓰면 시간초과
# que = deque()

# answer = 0

# start,end=0,int()

# for x,y in arr:

#     que.append([x,y])

#     if not start < x and x < end :
#         start,end=que.popleft()

# print(len(que))

