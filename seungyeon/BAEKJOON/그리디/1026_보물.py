# import sys
# input=sys.stdin.readline

# n = int(input())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))

# a.sort()
# sum = 0

# for i in range(n):
#     sum += max(b)*a[i]
#     b.remove(max(b))
# print(sum)

import sys,heapq
input=sys.stdin.readline
n=int(input())
a = sorted(list(map(int,input().split())))
b = list(map(int,input().split()))

que=[]

for i in b:
    heapq.heappush(que,-i)
sum = 0
for i in a:
    sum += i * (-1 * heapq.heappop(que))

print(sum)