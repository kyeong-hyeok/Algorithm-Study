# import sys
# import heapq
# input=sys.stdin.readline

# n = int(input().rstrip())
# arr=[]
# for i in range(n):
#     heapq.heappush(arr,int(input().rstrip()))

# if n == 1:
#     print(0)
# else :
#     sum = int(heapq.heappop(arr))
#     sum += int(heapq.heappop(arr))
#     while(arr):
#         x = int(heapq.heappop(arr))

#         sum += (x + sum)
        

#     print(sum)

import sys
import heapq
input=sys.stdin.readline


n = int(input().rstrip())
arr=[]
for i in range(n):
    heapq.heappush(arr,int(input().rstrip()))

sum = 0

while len(arr)>1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    k = first + second
    heapq.heappush(arr,k)
    sum += k

print(sum)