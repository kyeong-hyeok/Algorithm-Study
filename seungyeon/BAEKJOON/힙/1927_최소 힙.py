# import sys
# import heapq
# input=sys.stdin.readline

# n = int(input())
# arr=[]
# for i in range(n):
#     x = int(input())

#     if x == 0:
#            if not arr:
#                 print(0)
#            else:
#                 print(heapq.heappop(arr))
#     else:
#         heapq.heappush(arr,x)

import sys,heapq
input = sys.stdin.readline

n = int(input())

arr=[]
for i in range(n):
    k = int(input())

    if k == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr,k)
