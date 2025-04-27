# import sys
# n = int(input())
# arr = list(map(int,input().split()))

# answer =[0,0]

# left,right,m = 0,n-1,sys.maxsize

# while left < right:
#     if abs(arr[left]+ arr[right]) < m:
#         m = abs(arr[left]+arr[right])
#         answer[0] = arr[left]
#         answer[1] = arr[right]
#     if arr[left] + arr[right] < 0:
#         left += 1
#     else:
#         right -=1

# print(answer[0],answer[1])

import sys

n=int(input())
arr=list(map(int,input().split()))

l,r=0,n-1

ans = sys.maxsize
answer_l=0
answer_r=0
# 10만을 O(n)
while (l<r):

    if abs(arr[l]+arr[r]) < ans:
        ans = abs(arr[l]+arr[r])
        answer_l = arr[l]
        answer_r = arr[r]
    if arr[l]+arr[r] < 0:
        l += 1

    else:
        r -= 1
        
print(answer_l,answer_r)