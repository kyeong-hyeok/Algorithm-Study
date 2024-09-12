# import sys
# input=sys.stdin.readline

# n = int(input())


# arr = list(map(int,input().split()))

# m = int(1e9)
# index = 0
# for i in range(len(arr)):
#     if m > arr[i]:
#         m = arr[i]
#         index = i

# for i in range(n-1):
#     str=list(map(int,input().split()))

#     if i == n-2:
#         print(str[i])
import sys,heapq

input=sys.stdin.readline
n = int(input())

arr=[]

for i in range(n):
    str=list(map(int,input().split()))

    for i in str:
        if len(arr) < n:
            heapq.heappush(arr,i)
        else:
            if arr[0] < i: # 가장 작은 값을 갱신
                heapq.heappop(arr)
                heapq.heappush(arr,i)


print(arr[0]) # 그래서 가장 큰 값 5개만 남기고 그 중 가장 작은 값 프린트 