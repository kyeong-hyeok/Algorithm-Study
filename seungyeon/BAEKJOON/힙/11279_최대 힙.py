
    
import sys
import heapq
input=sys.stdin.readline

n=int(input())

que=[]

for i in range(n):
    x = int(input())
    if x == 0:
        if que:
            print(heapq.heappop(que)*(-1))
        else:
            print(0)
    else:
        heapq.heappush(que,x*(-1))

# 시간초과
        
# import sys
# import heapq
# input=sys.stdin.readline

# n=int(input())

# que=[]

# for i in range(n):
#     x = int(input())
#     if x == 0:
#         if que:
#             print(que[-1])
#             que.remove(que[-1])
#         else:
#             print(0)
#     else:
#         heapq.heappush(que,x)
