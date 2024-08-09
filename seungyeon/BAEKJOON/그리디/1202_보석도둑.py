import sys
import heapq

input=sys.stdin.readline

n,k = map(int,input().split())

jew = []
for i in range(n):
    weight,price = map(int,input().split())
    jew.append((weight,price))

bags=[]
for j in range(k):
    bags.append(int(input()))

jew.sort()
bags.sort()

heap = []

curr = 0
result = 0

for bag in bags:

    while curr < n:
        weight,price = jew[curr]

        if bag >= weight :
            heapq.heappush(heap,-price)
            curr += 1
        else :
            break
    if len(heap) >0 :
        result += heapq.heappop(heap) * (-1)

print(result)

