import heapq
import sys
input=sys.stdin.readline

n=int(input())

arr=[]
for i in range(n):
    k = int(input())
    if k == 0:
        # pop()
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else :
        heapq.heappush(arr,(abs(k),k))
